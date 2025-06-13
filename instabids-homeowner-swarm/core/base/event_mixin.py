# core/base/event_mixin.py
from typing import List

class EventMixin:
    """A mixin class to provide event handling capabilities to agents."""

    async def consume_events(self, streams: List[str], mcp, count: int = 10):
        """Consumes events from the specified Redis streams."""
        if not hasattr(self, 'event_consumer'):
            raise AttributeError("EventMixin requires an 'event_consumer' attribute.")
        return await self.event_consumer.consume(streams, mcp, count)

    async def publish_event(self, stream: str, event_type: str, data: dict, mcp):
        """Publishes an event to the specified Redis stream."""
        if not hasattr(self, 'event_publisher'):
            raise AttributeError("EventMixin requires an 'event_publisher' attribute.")
        return await self.event_publisher.publish(stream, event_type, data, mcp)
