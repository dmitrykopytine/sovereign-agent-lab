"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ['search_venues', 'get_venue_details']

QUERY_1_VENUE_NAME    = "The Haymarket Vaults"
QUERY_1_VENUE_ADDRESS = "1 Dalry Road, Edinburgh"
QUERY_2_FINAL_ANSWER  = """
It seems there are no Edinburgh venues currently available that can accommodate 300 people with vegan options. Would you like to:
1. Search for venues with a lower minimum capacity?
2. Look for venues without the vegan requirement?
3. Check availability for a different date?
"""

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
I changed the file sovereign_agent/tools/mcp_venue_server.py (changed availability of 
The Albanach to 'full').

I did not need to update week1/exercise4_mcp_client.py, as the change was related only 
to the tools available via MCP.

The result in my particular case did not change a lot, since the initial query responded 
with "The Haymarket Vaults", which is a valid answer for both queries (before and after 
making The Albanach 'full').
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

# Tools' function names in create_react_agent() call + related imports
LINES_OF_TOOL_CODE_EX2 = 8   # count in exercise2_langgraph.py
# discover_tools() function, the result is then sent to create_react_agent()
LINES_OF_TOOL_CODE_EX4 = 23   # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
Why MCP is better than hardcoded tools:
  - Automatic tool discovery - no need to hardcode tools and change agent's code when 
    tools change.
  - Tools can be improved separately from the agent (independent code/server) - easier 
    to maintain.
  - Not only separate file, but every tool may be launched on its own server on a 
    hardware/environment best for the tool - easier to scale.
"""

# ── PyNanoClaw architecture — SPECULATION QUESTION ─────────────────────────
#
# (The variable below is still called WEEK_5_ARCHITECTURE because the
# grader reads that exact name. Don't rename it — but read the updated
# prompt: the question is now about PyNanoClaw, the hybrid system the
# final assignment will have you build.)
#
# This is a forward-looking, speculative question. You have NOT yet seen
# the material that covers the planner/executor split, memory, or the
# handoff bridge in detail — that is what the final assignment (releases
# 2026-04-18) is for. The point of asking it here is to check that you
# have read PROGRESS.md and can imagine how the Week 1 pieces grow into
# PyNanoClaw.
#
# Read PROGRESS.md in the repo root. Then write at least 5 bullet points
# describing PyNanoClaw as you imagine it at final-assignment scale.
#
# Each bullet should:
#   - Name a component (e.g. "Planner", "Memory store", "Handoff bridge",
#     "Rasa MCP gateway")
#   - Say in one clause what that component does and which half of
#     PyNanoClaw it lives in (the autonomous loop, the structured agent,
#     or the shared layer between them)
#
# You are not being graded on getting the "right" architecture — there
# isn't one right answer. You are being graded on whether your description
# is coherent and whether you have thought about which Week 1 file becomes
# which PyNanoClaw component.
#
# Example of the level of detail we want:
#   - The Planner is a strong-reasoning model (e.g. Nemotron-3-Super or
#     Qwen3-Next-Thinking) that takes the raw task and produces an ordered
#     list of subgoals. It lives upstream of the ReAct loop in the
#     autonomous-loop half of PyNanoClaw, so the Executor never sees an
#     ambiguous task.

WEEK_5_ARCHITECTURE = """
Components:
  - Planner - strong-reasoning model, part of the autonomous loop. Top-level thinking model 
    which decides what to do next.
  - MCP server with research tools. Used by the autonomous loop. The tools may include:
    venue search, venue details (potentially split into fetch-parse-fetch-parse-...-return 
    logic), weather checker.
  - Memory store - remembers previous searches across sessions (for the autonomous loop), also 
    a shared layer to tranfer information between the autonomous loop and the structured agent.
    It may also keep results of conversations done with the structured agent.
  - Handoff bridge - routes human-conversation tasks to the structured-agent (a shared layer).
  - Interaction/observability layer. For both parts. Manages cost guiderails, logging,
    heartbeat. Accepts human input with the task and makes sure important details are passed 
    to the user: deposit, flyer URL, etc.
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
Research agent should be flexible. LangGraph or any other solution with the generic loop 
(LLM -> tools -> LLM -> ...) can work well for this.

For the call it's better to use something more structured like Rasa CALM. LLM is used 
there to parse natural language, but the flow is controlled by a strict algorithm. For example,
in ex3 Rasa CALM guaranteed all three variables (guest_count, vegan_count, deposit_amount_gbp) 
were collected before running the business logic.

Using research agent for the call would be risky (less predictable, less reliable).

Using the call agent/logic for research would be inefficient - too strict, requiring too much
domain-specific configuration. For example, in ex2 and ex4 LangGraph's LLM could decide which 
venues to check and in which order. Such flexibility is not possible or difficult to implement 
with the call agent/logic.
"""