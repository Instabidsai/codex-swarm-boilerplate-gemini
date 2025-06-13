import pytest
import json
from agents.homeowner_intake.nlp_processor import NLPProcessor

class DummyMCP:
    async def call_tool(self, tool_name: str, args: dict):
        return json.dumps({
            "project_type": "bathroom_remodel",
            "requirements": ["tile"],
            "budget_range": "$5000-$10000",
            "timeline": "2 months",
            "urgency": "normal"
        })

@pytest.mark.asyncio
async def test_extract_project_info():
    processor = NLPProcessor()
    mcp = DummyMCP()
    result = await processor.extract_project_info("Remodel my bathroom", mcp)
    assert result["project_type"] == "bathroom_remodel"
    assert result["requirements"] == ["tile"]
    assert result["budget_range"] == "$5000-$10000"
    assert result["timeline"] == "2 months"
    assert result["urgency"] == "normal"
    assert result["unclear_requirements"] == []

