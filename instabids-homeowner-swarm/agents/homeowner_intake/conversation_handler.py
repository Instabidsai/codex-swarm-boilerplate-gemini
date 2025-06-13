# agents/homeowner_intake/conversation_handler.py
import json

class ConversationHandler:
    """Handles multi-turn conversations with users to clarify project details."""

    def __init__(self):
        # In a real system, conversation memory would be stored in Redis.
        self.conversation_memory = {}

    async def needs_clarification(self, extracted_data: dict) -> bool:
        """Checks if the project requires clarification."""
        return bool(extracted_data.get("unclear_requirements"))

    async def request_clarification(self, project_id: str, unclear_items: list, mcp):
        """Publishes an event to the UI agent to ask the user for more information."""
        event_data = {
            "project_id": project_id,
            "type": "clarification_request",
            "message": f"To help you get the best bids, please provide more details on the following: {', '.join(unclear_items)}."
        }
        await mcp.call_tool("redis", {
            "command": "xadd",
            "stream": "ui:prompts",
            "fields": { "data": json.dumps(event_data) }
        })
