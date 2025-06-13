# core/events/publisher.py
import json
import uuid
from datetime import datetime

class EventPublisher:
    """Redis Streams event publisher using the MCP tool wrapper."""

    async def publish(self, stream: str, event_type: str, data: dict, mcp):
        """Publishes an event to a Redis Stream."""
        event = {
            'event_id': str(uuid.uuid4()),
            'event_type': event_type,
            'timestamp': datetime.utcnow().isoformat(),
            'data': json.dumps(data)
        }
        return await mcp.call_tool("redis", {
            "command": "xadd",
            "stream": stream,
            "fields": event
        })
