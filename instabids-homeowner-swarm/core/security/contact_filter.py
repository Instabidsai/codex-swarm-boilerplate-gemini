import re
from typing import Dict, List

EMAIL_PATTERN = re.compile(r"[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}")
PHONE_PATTERN = re.compile(r"\+?\d[\d\-\s]{7,}\d")

class ContactProtectionFilter:
    """A simplified contact protection scanner."""
    PHONE_PATTERNS = [r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b']
    EMAIL_PATTERNS = [r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b']

    def scan_content(self, content: str) -> Dict[str, List[str]]:
        """Scans content for phone numbers and emails."""
        violations = {"phones": [], "emails": []}
        for pattern in self.PHONE_PATTERNS:
            violations["phones"].extend(re.findall(pattern, content))
        for pattern in self.EMAIL_PATTERNS:
            violations["emails"].extend(re.findall(pattern, content))
        return violations


def mask_contact_info(text: str) -> str:
    """Mask phone numbers and emails in the given text."""
    text = EMAIL_PATTERN.sub("[REDACTED]", text)
    text = PHONE_PATTERN.sub("[REDACTED]", text)
    return text
