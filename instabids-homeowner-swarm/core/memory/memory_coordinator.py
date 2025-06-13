# core/memory/memory_coordinator.py

class MemoryCoordinator:
    """Coordinates memory operations across different tiers (Redis, Supabase)."""
    def __init__(self, event_store):
        self.event_store = event_store

    async def persist_event_from_stream(self, stream_event, mcp):
        """Takes an event from a Redis stream and persists it to the event store."""
        message_id, event_data = stream_event
        await self.event_store.store_event(event_data, mcp)
        print(f"Persisted event {event_data.get('event_id')} to Supabase.")
