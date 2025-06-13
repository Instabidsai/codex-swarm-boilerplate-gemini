import redis
from typing import Any


class RedisStore:
    """Simple wrapper around redis-py for key/value storage and event streams."""

    def __init__(self, url: str = "redis://localhost:6379/0"):
        self.redis = redis.from_url(url)

    def set(self, key: str, value: Any) -> bool:
        return self.redis.set(key, value)

    def get(self, key: str) -> Any:
        return self.redis.get(key)

    def xadd(self, stream: str, data: dict) -> str:
        return self.redis.xadd(stream, data)
