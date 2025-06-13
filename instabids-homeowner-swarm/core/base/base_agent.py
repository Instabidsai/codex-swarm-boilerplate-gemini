# core/base/base_agent.py
import asyncio
import uuid

class BaseAgent:
    """The base class for all agents in the swarm."""

    def __init__(self, agent_id: str, agent_type: str):
        self.agent_id = agent_id or f"{agent_type}_{uuid.uuid4()}"
        self.agent_type = agent_type
        self.is_running = False

    async def start(self):
        """Starts the agent's main processing loop."""
        self.is_running = True
        await self.start_processing()

    async def stop(self):
        """Stops the agent's main processing loop."""
        self.is_running = False

    async def start_processing(self):
        """The main processing loop for the agent. Must be overridden."""
        raise NotImplementedError("Subclasses must implement the start_processing method.")

    async def handle_error(self, error: Exception, mcp):
        """Handles any errors that occur during processing."""
        print(f"Error in {self.agent_id}: {error}")
        # This would publish to a high-priority system alert stream.
