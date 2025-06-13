import json
from typing import Any, Dict
import redis


class EventPublisher:
    """Publish events to a Redis stream."""

    def __init__(self, redis_url: str = "redis://localhost:6379/0", stream: str = "events"):
        self.redis = redis.from_url(redis_url)
        self.stream = stream

    def publish_event(self, event: Dict[str, Any]) -> str:
        """Publish a JSON-serializable event to the Redis stream."""
        data = json.dumps(event)
        return self.redis.xadd(self.stream, {"data": data})


def publish_event(event: Dict[str, Any], *, redis_url: str = "redis://localhost:6379/0", stream: str = "events") -> str:
    """Convenience function for publishing a single event."""
    publisher = EventPublisher(redis_url=redis_url, stream=stream)
    return publisher.publish_event(event)
