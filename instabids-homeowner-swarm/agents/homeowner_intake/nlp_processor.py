# agents/homeowner_intake/nlp_processor.py
from typing import List
from agents.homeowner_intake.intake_schemas import ExtractedProjectInfo
import json

class NLPProcessor:
    """Uses an LLM to perform Natural Language Processing on project descriptions."""

    async def extract_project_info(self, description: str, mcp) -> dict:
        """Extracts structured information from a raw project description using an LLM call."""
        extraction_prompt = f"""
        Extract the following information from this project description:

        Description: "{description}"

        Please extract:
        1.  Project type (e.g., bathroom remodel, kitchen, flooring)
        2.  Specific requirements (e.g., materials, styles, features)
        3.  Budget range (if mentioned)
        4.  Timeline preferences (if mentioned)
        5.  Urgency level (urgent, normal, flexible)

        Return as a JSON object with keys: "project_type", "requirements", "budget_range", "timeline", "urgency".
        """

        # This would be a call to an LLM tool like claude-code or a similar service
        result_json_str = await mcp.call_tool("context7", {
            "query": extraction_prompt
        })

        try:
            # In a real scenario, you would parse the LLM's JSON string output.
            # Add robust JSON parsing and error handling here.
            extracted = json.loads(result_json_str) if result_json_str else {}
        except (json.JSONDecodeError, TypeError):
            # Fallback for simulation or if the LLM fails
            extracted = {"project_type": "simulated_remodel", "requirements": ["simulated_tile"]}

        extracted_data = ExtractedProjectInfo(**extracted)
        extracted_data.unclear_requirements = self._identify_unclear_items(extracted_data)

        return extracted_data.dict()

    def _identify_unclear_items(self, extracted_data: ExtractedProjectInfo) -> List[str]:
        """Identifies which key pieces of information are still missing."""
        unclear = []
        if not extracted_data.budget_range:
            unclear.append("budget_range")
        if not extracted_data.timeline:
            unclear.append("timeline")
        if extracted_data.project_type == "unknown":
            unclear.append("project_type")
        return unclear
