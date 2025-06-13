# 🤖 AGENT ASSIGNMENTS

This document outlines the specific build paths for each of the 6 AI agents responsible for constructing the Instabids Homeowner Agent Swarm.

---

## AGENT 1: CORE INFRASTRUCTURE BUILDER

**🎯 RESPONSIBILITY:** Build the foundational infrastructure that all other agents depend on.
**📁 YOUR DOMAIN:** `core/`, `deployment/`

---

## AGENT 2: HOMEOWNER INTAKE BUILDER

**🎯 RESPONSIBILITY:** Build the natural language processing for homeowner project intake.
**📁 YOUR DOMAIN:** `agents/homeowner_intake/`, `tests/agent_specific/test_intake_agent.py`

---

## AGENT 3: PROJECT SCOPE BUILDER

**🎯 RESPONSIBILITY:** Convert intake data into structured project scopes.
**📁 YOUR DOMAIN:** `agents/project_scope/`, `tests/agent_specific/test_scope_agent.py`

---

## AGENT 4: COMMUNICATION FILTER BUILDER

**🎯 RESPONSIBILITY:** Build the multi-layer contact protection system.
**📁 YOUR DOMAIN:** `agents/communication_filter/`, `tests/agent_specific/test_filter_agent.py`

---

## AGENT 5: PAYMENT GATE BUILDER

**🎯 RESPONSIBILITY:** Build the payment processing system that controls contact information release.
**📁 YOUR DOMAIN:** `agents/payment_gate/`, `tests/agent_specific/test_payment_agent.py`

---

## AGENT 6: UI GENERATOR BUILDER

**🎯 RESPONSIBILITY:** Build the dynamic, agent-aware UI using CopilotKit.
**📁 YOUR DOMAIN:** `agents/ui_generator/`, `ui/`, `tests/agent_specific/test_ui_agent.py`
