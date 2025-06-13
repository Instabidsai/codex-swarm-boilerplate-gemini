# 🌊 INSTABIDS HOMEOWNER AGENT SWARM

**Building the world's first living AI organism - starting with the Homeowner Agent Swarm as a proof of concept.**

This repository contains the complete build plan and source structure for the Instabids Homeowner Agent Swarm. It's designed for a team of AI agents to collaboratively build, test, and deploy a complex, event-driven system.

## 🤖 QUICK START FOR AI AGENTS

### Your Agent Assignment:
- **Agent 1-6:** Check `AGENT_ASSIGNMENTS.md` for your specific domain and build path.
- **Build Order:** Agent 1 → Agents 2-4 (in parallel) → Agents 5-6 (in parallel).
- **Tools:** Use MCP tools as specified in `MCP_TOOLS_REFERENCE.md`.

### Critical Rules:
- ❌ **NO** direct agent communication. Use Redis Streams only.
- 🛡️ Contact information protection is **ABSOLUTE**. This is the core of the business model.
- 💰 Cost limits are **$0.05/event** and **$1000/day**.
- 📝 Update `build_coordination/build_status.json` after each of your build phases.

---

## 📁 PROJECT STRUCTURE
<!-- AUTO-GENERATED - DO NOT EDIT MANUALLY -->
<!-- Use: tree -I '__pycache__|.git|node_modules' -L 3 > temp && insert into README -->


instabids-homeowner-swarm/
├── README.md
├── AGENT_ASSIGNMENTS.md
├── MCP_TOOLS_REFERENCE.md
├── ARCHITECTURE_GUIDE.md
├── CODEBASE_MANIFEST.json
├── build_coordination/
│   ├── build_status.json
│   ├── agent_dependencies.json
│   └── agent_handoff_manifest.json
├── core/
│   ├── base/
│   ├── events/
│   ├── memory/
│   └── security/
├── agents/
│   ├── homeowner_intake/
│   ├── project_scope/
│   ├── communication_filter/
│   ├── payment_gate/
│   └── ui_generator/
├── ui/
│   ├── src/
│   │   ├── components/
│   │   ├── hooks/
│   │   └── pages/
│   └── public/
├── tests/
│   ├── agent_specific/
│   ├── e2e/
│   ├── integration/
│   ├── performance/
│   └── security/
└── deployment/
    ├── postgres/
    └── scripts/

---

## 🧪 TESTING STRATEGY

- **Frameworks:** `pytest` and `asyncio` for Python, `Jest` for TypeScript.
- **Location:** All tests are located in the `tests/` directory, with subdirectories for different types of testing.
- **Run Tests:** `python -m pytest tests/`
- **Required Coverage:** >80% for all agent domains.
- **Security Tests:** The contact protection system must have a 100% block rate.

---

## 🚀 QUICK DEPLOYMENT

### Prerequisites:
- **Redis:** Already configured at DigitalOcean (see `MCP_TOOLS_REFERENCE.md`).
- **Supabase:** Use the provided API token.
- **MCP Tools:** Pre-configured (see `CODEBASE_MANIFEST.json`).

### Start Building:
1.  Check `build_coordination/build_status.json` for the current progress.
2.  Follow your assignment in `AGENT_ASSIGNMENTS.md`.
3.  Use MCP tools as documented in `MCP_TOOLS_REFERENCE.md`.
4.  Test continuously with `python -m pytest tests/agent_specific/`.
