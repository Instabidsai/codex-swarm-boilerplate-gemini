import json
import asyncio
from typing import AsyncGenerator, Dict, Any
import redis.asyncio as aioredis


class EventSubscriber:
    """Consume events from a Redis stream."""

    def __init__(self, redis_url: str = "redis://localhost:6379/0", stream: str = "events"):
        self.redis = aioredis.from_url(redis_url)
        self.stream = stream
        self.last_id = "$"

    async def consume_events(self) -> AsyncGenerator[Dict[str, Any], None]:
        while True:
            resp = await self.redis.xread({self.stream: self.last_id}, block=1000, count=1)
            if resp:
                _, messages = resp[0]
                message_id, data = messages[0]
                self.last_id = message_id
                payload = json.loads(data[b"data"].decode())
                yield payload
            else:
                await asyncio.sleep(0.1)


async def consume_events(redis_url: str = "redis://localhost:6379/0", stream: str = "events") -> AsyncGenerator[Dict[str, Any], None]:
    subscriber = EventSubscriber(redis_url=redis_url, stream=stream)
    async for event in subscriber.consume_events():
        yield event
