# core/security/cost_breaker.py
class CostCircuitBreaker:
    """A circuit breaker to prevent runaway AI costs."""
    def __init__(self, daily_limit: float = 1000.0, per_event_limit: float = 0.05):
        self.daily_limit = daily_limit
        self.per_event_limit = per_event_limit
        self.daily_cost = 0.0  # This would be fetched from a central store

    async def check_cost_approval(self, estimated_cost: float, mcp) -> bool:
        """Checks if a proposed action's cost is within limits."""
        if estimated_cost > self.per_event_limit:
            print(f"COST VIOLATION: Per-event limit exceeded. Cost: ${estimated_cost}")
            return False
        if self.daily_cost + estimated_cost > self.daily_limit:
            print("EMERGENCY SHUTDOWN: Daily cost limit exceeded.")
            return False
        return True
