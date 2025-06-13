# core/security/audit_logger.py
class AuditLogger:
    """Logs critical security and compliance events to a dedicated audit trail."""
    def __init__(self, table_name: str = "audit_logs"):
        self.table_name = table_name

    async def log(self, actor: str, action: str, details: dict, mcp):
        """Creates an audit log entry."""
        log_entry = {"actor": actor, "action": action, "details": details}
        await mcp.call_tool("supabase", {
            "action": "insert",
            "table": self.table_name,
            "data": [log_entry]
        })
