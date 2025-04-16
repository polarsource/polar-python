import atexit
import contextlib
import logging
import queue
import threading
import time
from collections.abc import Callable
from typing import TYPE_CHECKING, Union

from polar_sdk import Polar

if TYPE_CHECKING:
    from polar_sdk import EventsModelTypedDict

logger = logging.getLogger("polar_sdk.ingestion")


class Ingestion:
    """
    Event ingestion client for Polar.

    This class handles the ingestion of events into the Polar API without blocking
    the main thread, by using background thread sending them in batches.

    :param access_token: The access_token required for authentication
    :param server: The server by name to use for all methods
    :param server_url: The server URL to use for all methods
    :param max_batch_size: The maximum number of events to send in a single batch.
    :param flush_interval: The interval in seconds to wait before flushing events.
    :param max_queue_size: The maximum number of events to keep in the queue.
    """

    def __init__(
        self,
        access_token: Union[str, Callable[[], Union[str, None]], None] = None,
        server: Union[str, None] = None,
        server_url: Union[str, None] = None,
        *,
        max_batch_size: int = 50,
        flush_interval: float = 5.0,
        max_queue_size: int = 10000,
    ) -> None:
        self.max_batch_size = max_batch_size
        self.flush_interval = flush_interval
        self.max_queue_size = max_queue_size

        self._stack = contextlib.ExitStack()
        self._client = self._stack.enter_context(
            Polar(access_token, server, server_url)
        )

        self._queue = queue.Queue["EventsModelTypedDict"](maxsize=max_queue_size)

        self._thread = threading.Thread(target=self._worker, daemon=True)
        self._thread_running = threading.Event()
        self._thread_running.set()
        self._thread.start()

        atexit.register(self.close)

    def ingest(self, event: "EventsModelTypedDict") -> None:
        """
        Send an event to the ingestion queue.

        :param event: The event to send.
        """
        self._queue.put(event, block=False)

    def flush(self, max_batch_size: Union[int, None] = None) -> None:
        """
        Flush events from the queue to the API

        :param max_batch_size: The maximum number of events to send in the batch.
        If `None`, there is no limit.
        """
        if self._queue.empty():
            return

        # Collect events up to max_batch_size
        events: list[EventsModelTypedDict] = []
        try:
            while not self._queue.empty() and (
                max_batch_size is None or len(events) < max_batch_size
            ):
                events.append(self._queue.get_nowait())
        except queue.Empty:
            pass

        if not events:
            return

        # Send the batch to the API
        try:
            self._send_batch(events)
            # Mark tasks as done only after successful sending
            for _ in events:
                self._queue.task_done()
        except Exception as e:
            # On failure, put events back in the queue for retry
            logger.error("Failed to send events: %s", e)
            for event in events:
                try:
                    self._queue.put(event, block=False)
                except queue.Full:
                    logger.error("Queue full, dropping event during retry")

    def close(self) -> None:
        """
        Flush remaining events and close the background thread.

        It's called automatically on program exit.
        """
        logger.debug("Shutting down, flushing remaining events...")
        self._thread_running.clear()

        # Try to flush remaining events
        try:
            self.flush()
        except Exception as e:
            logger.error("Error during shutdown flush: %s", e)

        if self._thread.is_alive():
            self._thread.join(timeout=5.0)

        self._stack.close()
        logger.debug("Shutdown complete")

    def _worker(self) -> None:
        logger.debug("Worker thread started")
        while self._thread_running.is_set():
            try:
                self.flush(self.max_batch_size)
            except Exception as e:
                logger.error("Error in worker thread: %s", e)

            time.sleep(self.flush_interval)

    def _send_batch(self, events: list["EventsModelTypedDict"]) -> None:
        response = self._client.events.ingest(request={"events": events})
        logger.debug("Ingested %d events", response.inserted)
