# 🏗️ ARCHITECTURE GUIDE

This document outlines the system design principles for the Instabids Homeowner Agent Swarm.

## 3-Tier Memory System

1.  **Tier 1: Redis** - Real-time events, agent coordination, and temporary state.
2.  **Tier 2: Supabase** - Event store for an audit trail and read models for fast queries.
3.  **Tier 3: Dynamic UI** - CopilotKit, morphing based on agent activity.

## Event-Driven Core

- **NO** direct agent communication. Agents **ONLY** communicate through Redis Stream events.
- A complete audit trail of every action is stored indefinitely.
- The system is self-organizing, with agents spawning based on queue depth.
- The system is self-healing, with automatic recovery from failures.

## Agentic Coordination Patterns

- **Handoffs:** Agent handoffs are managed through a `handoffProtocol` defined in `CODEBASE_MANIFEST.json`.
- **Status Tracking:** The build status is tracked in `build_coordination/build_status.json`.
- **Dependencies:** Agent dependencies are explicitly defined in `build_coordination/agent_dependencies.json`.
