import pytest
from core.security.contact_filter import mask_contact_info


def test_mask_email():
    text = "Contact me at john@example.com"
    assert mask_contact_info(text) == "Contact me at [REDACTED]"


def test_mask_phone():
    text = "Call me at 555-123-4567 for info"
    assert mask_contact_info(text) == "Call me at [REDACTED] for info"
