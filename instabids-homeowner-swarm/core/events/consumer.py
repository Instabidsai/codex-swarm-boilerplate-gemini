# core/events/consumer.py
from typing import List

class EventConsumer:
    """Redis Streams consumer with consumer group support using MCP."""

    def __init__(self, consumer_group: str, consumer_name: str):
        self.consumer_group = consumer_group
        self.consumer_name = consumer_name

    async def consume(self, streams: List[str], mcp, count: int = 10):
        """Consumes events from a list of streams for the configured consumer group."""
        stream_dict = {stream: '>' for stream in streams}
        return await mcp.call_tool("redis", {
            "command": "xreadgroup",
            "group": self.consumer_group,
            "consumer": self.consumer_name,
            "streams": stream_dict,
            "count": count
        })
