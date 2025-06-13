# core/events/coordinator.py

class EventCoordinator:
    """Manages the setup of Redis streams and consumer groups."""
    def __init__(self, streams_and_groups: dict):
        self.streams_and_groups = streams_and_groups

    async def setup_streams(self, mcp):
        """Creates all necessary streams and consumer groups using MCP."""
        print("Setting up Redis streams and consumer groups...")
        for stream, groups in self.streams_and_groups.items():
            for group in groups:
                try:
                    await mcp.call_tool("redis", {
                        "command": "xgroup_create",
                        "stream": stream,
                        "group": group,
                        "id": "$",
                        "mkstream": True
                    })
                    print(f"Created group '{group}' on stream '{stream}'.")
                except Exception as e:
                    if "BUSYGROUP" in str(e):
                        print(f"Group '{group}' on stream '{stream}' already exists.")
                    else:
                        print(f"Error creating group '{group}' on stream '{stream}': {e}")
        print("Stream setup complete.")
