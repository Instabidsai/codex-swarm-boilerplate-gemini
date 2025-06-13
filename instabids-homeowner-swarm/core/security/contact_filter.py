import re

EMAIL_PATTERN = re.compile(r"[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}")
PHONE_PATTERN = re.compile(r"\+?\d[\d\-\s]{7,}\d")


def mask_contact_info(text: str) -> str:
    """Mask phone numbers and emails in the given text."""
    text = EMAIL_PATTERN.sub("[REDACTED]", text)
    text = PHONE_PATTERN.sub("[REDACTED]", text)
    return text
