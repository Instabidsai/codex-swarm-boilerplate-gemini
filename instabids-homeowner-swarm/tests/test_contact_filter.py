from core.security.contact_filter import ContactProtectionFilter


def test_scan_email():
    text = "Contact me at john@example.com"
    violations = ContactProtectionFilter().scan_content(text)
    assert violations["emails"] == ["john@example.com"]


def test_scan_phone():
    text = "Call me at 555-123-4567 for info"
    violations = ContactProtectionFilter().scan_content(text)
    assert violations["phones"] == ["555-123-4567"]
