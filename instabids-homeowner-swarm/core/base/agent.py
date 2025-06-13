from __future__ import annotations
import asyncio
from abc import ABC, abstractmethod
from typing import AsyncGenerator, Dict, Any
import redis.asyncio as aioredis
from ..events.publisher import EventPublisher
from ..events.subscriber import EventSubscriber


class BaseAgent(ABC):
    """Base class providing event publishing and consuming helpers."""

    def __init__(self, redis_url: str = "redis://localhost:6379/0", stream: str = "events"):
        self.publisher = EventPublisher(redis_url=redis_url, stream=stream)
        self.subscriber = EventSubscriber(redis_url=redis_url, stream=stream)

    async def publish(self, event: Dict[str, Any]) -> str:
        return self.publisher.publish_event(event)

    async def consume(self) -> AsyncGenerator[Dict[str, Any], None]:
        async for event in self.subscriber.consume_events():
            yield event

    @abstractmethod
    async def run(self) -> None:
        """Run the agent."""
        raise NotImplementedError
