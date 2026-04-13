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
QUERY_2_FINAL_ANSWER  = "It appears that there are no available venues in Edinburgh that can accommodate 300 people, regardless of dietary requirements. The search results are empty."

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
Changed file sovereign_agent/tools/mcp_venue_server.py
Changed availability of The Albanach to 'full'.
After that I ran the experiment again.
Then I reverted the change.
The result in my particular case did not change a lot, since the initial query responded with "The Haymarket Vaults", which is a valid answer for both queries (before and after making The Albanach 'full').
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 8   # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 0   # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
Automatic tool discovery - no need to hardcode tools and change agent's code when tools change.
Tools can be improved separately from the agent (independent code/server) - easier to maintain.
Not only separate file, but every tool may be launched on its own server on a hardware/environment best for the tool - easier to scale.
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
- Web search - actual search the web for Edinburgh pubs, reading venue websites.
- Memory via CLAUDE.md - remember previous searches across sessions, learn from past bookings.
- Planner-Executor architecture - plan autonomously: search → filter → verify → book → generate flyer.
- Security sandboxing - make sure all external communications are safe and do not compromise the system.
- Cost guardrails - prevent the agent from booking too expensive venues.
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
The research agent needs better flexibility.
LangGraph or and other solution with the loop (LLM -> tools -> LLM -> ...) can do this.
Example include LangGraph from exercise2 or exercise4 (with manually added tools or automatic MCP-based tool discovery).

For the call it's better to use something more structured like Rasa CALM.
The reason - better predictability, connection with the buisiness domain (specific flows, parameters).
Better for specific jobs with clear in/outs which need to be executed in a call (or chat) as a question-answer chain.
LLM is used to parse natural language, but the flow is controlled by a strict algorithm.
Example is exercise3.
"""