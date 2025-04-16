from typing import Any, TypeVar

from .._base import Ingestion


class BaseStrategy:
    """
    Base structure of an event ingestion strategy.

    :param event_name: The name of the events that'll be reported by the strategy.
    :param ingestion: The ingestion client to use for sending events.
    """

    def __init__(self, event_name: str, ingestion: Ingestion) -> None:
        self.event_name = event_name
        self._ingestion = ingestion

    def ingest(self, external_customer_id: str, *args: Any, **kwargs: Any) -> None:
        """
        Send an event to the ingestion queue.

        :param external_customer_id: The external customer ID to associate with the event.
        """
        raise NotImplementedError()


S = TypeVar("S", bound=BaseStrategy)
