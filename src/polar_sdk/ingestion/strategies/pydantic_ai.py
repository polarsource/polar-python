from typing import Any

from pydantic_ai.agent import AgentRunResult

from ._base import BaseStrategy


class PydanticAIStrategy(BaseStrategy):
    """
    An ingestion strategy to report usage from PydanticAI agent runs.
    """

    def ingest(self, external_customer_id: str, result: AgentRunResult[Any]) -> None:
        """
        Report usage from a PydanticAI agent run.

        :param external_customer_id: The external customer ID to associate with the event.
        :param result: The result of the agent run.
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
                },
            }
        )
