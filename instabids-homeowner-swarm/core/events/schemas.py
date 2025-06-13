# core/events/schemas.py
from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import Dict, Any

class BaseEvent(BaseModel):
    """A base model for all events for validation purposes."""
    event_id: UUID4
    event_type: str
    timestamp: datetime
    data: Dict[str, Any]
