from typing import Any

from pydantic_ai.agent import AgentRunResult
from pydantic_ai.models import TYPE_CHECKING

from ._base import BaseStrategy

if TYPE_CHECKING:
    from polar_sdk import EventCreateCustomerMetadataTypedDict


class PydanticAIStrategy(BaseStrategy):
    """
    An ingestion strategy to report usage from PydanticAI agent runs.
    """

    def ingest(  # pylint: disable=W
        self,
        external_customer_id: str,
        result: AgentRunResult[Any],
        **metadata: "EventCreateCustomerMetadataTypedDict",
    ) -> None:
        """
        Report usage from a PydanticAI agent run.

        :param external_customer_id: The external customer ID to associate with the event.
        :param result: The result of the agent run.
        :param metadata: Extra metadata to include with the event.
        """
        usage = result.usage()
        self._ingestion.ingest(
            {
                "name": self.event_name,
                "external_customer_id": external_customer_id,
                "metadata": {
                    "request_tokens": usage.request_tokens or 0,
                    "response_tokens": usage.response_tokens or 0,
                    "total_tokens": usage.total_tokens or 0,
                    "requests": usage.requests or 0,
                    **self._metadata,
                    **metadata,
                },
            }
        )
