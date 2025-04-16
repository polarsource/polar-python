from typing import TYPE_CHECKING, Any, TypeVar, Union

from .._base import Ingestion

if TYPE_CHECKING:
    from polar_sdk import EventCreateCustomerMetadataTypedDict


class BaseStrategy:
    """
    Base structure of an event ingestion strategy.

    :param event_name: The name of the events that'll be reported by the strategy.
    :param ingestion: The ingestion client to use for sending events.
    :param metadata: Extra metadata to include with all events.
    """

    def __init__(
        self,
        event_name: str,
        ingestion: Ingestion,
        metadata: Union[dict[str, "EventCreateCustomerMetadataTypedDict"], None] = None,
    ) -> None:
        self.event_name = event_name
        self._ingestion = ingestion
        self._metadata = metadata or {}

    def ingest(self, external_customer_id: str, *args: Any, **kwargs: Any) -> None:
        """
        Send an event to the ingestion queue.

        :param external_customer_id: The external customer ID to associate with the event.
        """
        raise NotImplementedError()


S = TypeVar("S", bound=BaseStrategy)
