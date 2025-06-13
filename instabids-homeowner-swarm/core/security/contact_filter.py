# core/security/contact_filter.py
import re
from typing import Dict, List

class ContactProtectionFilter:
    """A simplified version of the contact protection filter."""
    # The full, multi-layer implementation is in the communication_filter agent.
    # This core version provides a basic pattern check.

    PHONE_PATTERNS = [r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b']
    EMAIL_PATTERNS = [r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b']

    def scan_content(self, content: str) -> Dict[str, List[str]]:
        """Scans content for basic phone and email patterns."""
        violations = {"phones": [], "emails": []}
        for pattern in self.PHONE_PATTERNS:
            violations["phones"].extend(re.findall(pattern, content))
        for pattern in self.EMAIL_PATTERNS:
            violations["emails"].extend(re.findall(pattern, content))
        return violations
