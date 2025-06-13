import asyncpg
from typing import Any, List, Dict


class PostgresStore:
    """Async wrapper for event storage in Postgres."""

    def __init__(self, dsn: str):
        self.dsn = dsn
        self.pool: asyncpg.Pool | None = None

    async def connect(self) -> None:
        if not self.pool:
            self.pool = await asyncpg.create_pool(dsn=self.dsn)

    async def save_event(self, event: Dict[str, Any]) -> None:
        await self.connect()
        async with self.pool.acquire() as conn:
            await conn.execute(
                "INSERT INTO events(data) VALUES($1)",
                event
            )

    async def fetch_events(self, limit: int = 100) -> List[Dict[str, Any]]:
        await self.connect()
        async with self.pool.acquire() as conn:
            rows = await conn.fetch("SELECT data FROM events ORDER BY id DESC LIMIT $1", limit)
        return [r["data"] for r in rows]
