# agents/homeowner_intake/intake_schemas.py
from pydantic import BaseModel, Field
from typing import List, Optional

class ExtractedProjectInfo(BaseModel):
    """Defines the structured data extracted from a user's project description."""
    project_type: str = Field(default="unknown", description="The type of project, e.g., bathroom_remodel.")
    requirements: List[str] = Field(default_factory=list, description="Specific requirements mentioned by the user.")
    budget_range: Optional[str] = Field(default=None, description="The user's stated budget.")
    timeline: Optional[str] = Field(default=None, description="The user's stated timeline.")
    urgency: str = Field(default="normal", description="The urgency of the project.")
    unclear_requirements: List[str] = Field(default_factory=list, description="Items that need further clarification.")
