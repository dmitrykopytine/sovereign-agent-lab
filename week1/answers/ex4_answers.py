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

# ── Week 5 architecture ────────────────────────────────────────────────────
# Describe your full sovereign agent at Week 5 scale.
# At least 5 bullet points. Each bullet must be a complete sentence
# naming a component and explaining why that component does that job.

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
