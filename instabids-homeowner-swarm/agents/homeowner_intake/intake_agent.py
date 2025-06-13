# agents/homeowner_intake/intake_agent.py
import asyncio
import json
from core.base.base_agent import BaseAgent
from core.events.publisher import EventPublisher
from core.events.consumer import EventConsumer
from core.security.contact_filter import ContactProtectionFilter
from agents.homeowner_intake.nlp_processor import NLPProcessor
from agents.homeowner_intake.conversation_handler import ConversationHandler

class HomeownerIntakeAgent(BaseAgent):
    """Processes homeowner project submissions, extracts data, and handles conversations."""

    def __init__(self, agent_id: str = "homeowner_intake_001"):
        super().__init__(agent_id, "homeowner_intake")
        self.nlp_processor = NLPProcessor()
        self.contact_filter = ContactProtectionFilter()
        self.conversation_handler = ConversationHandler()
        self.event_publisher = EventPublisher()
        self.event_consumer = EventConsumer(
            consumer_group="intake_processors",
            consumer_name=self.agent_id
        )

    async def start_processing(self, mcp):
        """Main event processing loop."""
        print(f"Agent {self.agent_id} starting...")
        while self.is_running:
            try:
                # The mcp tool call will return a list of streams with their messages
                events = await self.event_consumer.consume(
                    streams=["homeowner:project_submitted"], mcp=mcp
                )
                if events:
                    for stream, messages in events:
                        for message_id, data in messages:
                            # The 'data' field from Redis is often bytes, needs decoding
                            decoded_data = {k.decode('utf-8'): v.decode('utf-8') for k, v in data.items()}
                            payload = json.loads(decoded_data.get('data', '{}'))
                            await self.process_submission(payload, mcp)
                            await mcp.call_tool("redis", {
                                "command": "xack",
                                "stream": stream.decode('utf-8'),
                                "group": "intake_processors",
                                "id": message_id.decode('utf-8')
                            })
                await asyncio.sleep(1)
            except Exception as e:
                await self.handle_error(e, mcp)
                await asyncio.sleep(5)

    async def process_submission(self, project_data: dict, mcp):
        """Handles a single project submission."""
        description = project_data.get("description", "")
        project_id = project_data.get("project_id")

        # 1. Security Screening
        security_violations = self.contact_filter.scan_content(description)
        if any(security_violations.values()):
            # Publish a security violation event
            await self.event_publisher.publish("security:violation", "contact_info_detected", {
                "project_id": project_id,
                "violations": security_violations
            }, mcp)
            return

        # 2. Extract Information
        extracted_data = await self.nlp_processor.extract_project_info(description, mcp)

        # 3. Store extracted data (e.g., in a Supabase read model)
        await mcp.call_tool("supabase", {
            "action": "update",
            "table": "projects",
            "match": {"id": project_id},
            "data": {"intake_data": json.dumps(extracted_data), "status": "intake_processing"}
        })

        # 4. Check if clarification is needed
        if await self.conversation_handler.needs_clarification(extracted_data):
            await self.conversation_handler.request_clarification(
                project_id, extracted_data["unclear_requirements"], mcp
            )
        else:
            # 5. Publish completion event for the next agent
            await self.event_publisher.publish("homeowner:intake_complete", "intake_complete", {
                "project_id": project_id,
                "data": extracted_data
            }, mcp)
