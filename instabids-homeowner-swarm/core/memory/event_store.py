# core/memory/event_store.py
import json

class EventStore:
    """Handles the storage of all events to Supabase for a permanent audit trail."""
    def __init__(self, table_name: str = "events"):
        self.table_name = table_name

    async def store_event(self, event: dict, mcp):
        """Stores a single event in the Supabase event store table."""
        if isinstance(event.get('data'), dict):
            event['data'] = json.dumps(event['data'])

        await mcp.call_tool("supabase", {
            "action": "insert",
            "table": self.table_name,
            "data": [event]
        })
