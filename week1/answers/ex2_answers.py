"""
Exercise 2 — Answers
====================
Fill this in after running exercise2_langgraph.py.
Run `python grade.py ex2` to check for obvious issues.
"""

# ── Task A ─────────────────────────────────────────────────────────────────

# List of tool names called during Task A, in order of first appearance.
# Look at [TOOL_CALL] lines in your terminal output.
# Example: ["check_pub_availability", "get_edinburgh_weather"]

TASK_A_TOOLS_CALLED = ["check_pub_availability", "check_pub_availability", "calculate_catering_cost", "get_edinburgh_weather", "generate_event_flyer"]

# Which venue did the agent confirm? Must be one of:
# "The Albanach", "The Haymarket Vaults", or "none"
TASK_A_CONFIRMED_VENUE = "The Albanach"

# Total catering cost the agent calculated. Float, e.g. 5600.0
# Write 0.0 if the agent didn't calculate it.
TASK_A_CATERING_COST_GBP = 5600.0

# Did the weather tool return outdoor_ok = True or False?
TASK_A_OUTDOOR_OK = True

# Optional — anything unexpected.
# If you used a non-default model via RESEARCH_MODEL env var, note it here.
# Example: "Used nvidia/nemotron-3-super-120b-a12b for the agent loop."
TASK_A_NOTES = ""

# ── Task B ─────────────────────────────────────────────────────────────────

#
# The scaffold ships with a working generate_event_flyer that has two paths:
#
#   - Live mode: if FLYER_IMAGE_MODEL is set in .env, the tool calls that
#     model and returns a real image URL.
#   - Placeholder mode: otherwise (the default) the tool returns a
#     deterministic placehold.co URL with mode="placeholder".
#
# Both paths return success=True. Both count as "implemented" for grading.
# This is not the original Task B — the original asked you to write a direct
# FLUX image call, but Nebius removed FLUX on 2026-04-13. See CHANGELOG.md
# §Changed for why we pivoted the task.

# Did your run of the flyer tool produce a success=True result?
# (This will be True for both live and placeholder mode — both are valid.)
TASK_B_IMPLEMENTED = True   # True or False

# Which path did your run take? "live" or "placeholder"
# Look for the "mode" field in the TOOL_RESULT output of Task B.
# If you didn't set FLYER_IMAGE_MODEL in .env, you will get "placeholder".
TASK_B_MODE = "placeholder"

# The image URL returned by the tool. Copy exactly from your terminal output.
# In placeholder mode this will be a placehold.co URL.
# In live mode it will be a provider CDN URL.
TASK_B_IMAGE_URL = "https://placehold.co/1200x628/1a1a2e/eaeaea?text=The+Haymarket+Vaults+%7C+160+guests&id=2ef939fbbaf6"

# The prompt sent to the image model. Copy from terminal output.
TASK_B_PROMPT_USED = "Professional event flyer for Edinburgh AI Meetup, tech professionals, modern venue at The Haymarket Vaults, Edinburgh. 160 guests tonight. Warm lighting, Scottish architecture background, clean modern typography."

# Why did the agent's behaviour NOT change when Nebius removed FLUX?
# One sentence. This is the point of the lesson.
TASK_B_WHY_AGENT_SURVIVED = """
Fallback mechanism worked (deterministic placeholder) and returned success=True + image URL.
So the agent was able to continue the flow.
"""

# ── Task C ─────────────────────────────────────────────────────────────────

# Scenario 1: first choice unavailable
# Quote the specific message where the agent changed course. Min 20 words.
SCENARIO_1_PIVOT_MOMENT = """
The agent launched check_pub_availability() for The Bow Bar first, and it returned meets_all_constraints=false.
Then it checked The Albanach which satisfied all criteria, meets_all_constraints=true.
Based on the second call result the model chose The Albanach as the venue.

Quotes from the terminal output:

...
  [TOOL_CALL]    → check_pub_availability({"pub_name": "The Bow Bar", "required_capacity": 160, "requires_vegan": true})
  [TOOL_RESULT]  ← check_pub_availability: {"success": true, "pub_name": "The Bow Bar", "address": "80 West Bow, Edinburgh", "capacity": 80, "vegan": true, "status": "full", "meets_all_constraints": false}
...
  <think>
Okay, let's see. The user wanted to check The Bow Bar first for 160 vegan guests. The first tool call showed that The Bow Bar's capacity is only 80, which is too small. So then I checked The Albanach next. 
...
"""

SCENARIO_1_FALLBACK_VENUE = "The Albanach"

# Scenario 2: impossible constraint (300 guests)
# Did the agent recommend a pub name not in the known venues list?
SCENARIO_2_HALLUCINATED = False   # True or False

# Paste the final [AI] message.
SCENARIO_2_FINAL_ANSWER = """
None of the four known Edinburgh venues can accommodate 300 people with vegan options:
- The Albanach (180 capacity, vegan available)
- Haymarket Vaults (160 capacity, vegan available)
- Guilford Arms (200 capacity, no vegan)
- Bow Bar (80 capacity, vegan available but full)

Would you like me to:
1. Suggest alternative venues outside this list?
2. Help adjust requirements (e.g. split event across multiple venues)?
3. Check availability for a different date?
"""

# Scenario 3: out of scope (train times)
# Did the agent try to call a tool?
SCENARIO_3_TRIED_A_TOOL = False   # True or False

SCENARIO_3_RESPONSE = """
I don't have access to real-time train schedules or transportation data. For the most accurate information about the last train from Edinburgh Waverley to London, I recommend checking:
1. The National Rail website (https://www.nationalrail.co.uk)
2. Train service apps like Citymapper or Trainline
3. The specific train operator's website (e.g., LNER)

Would you like help with anything related to Edinburgh pubs, weather, or event planning instead?
"""

# Would this behaviour be acceptable in a real booking assistant? Min 30 words.
SCENARIO_3_ACCEPTABLE = """
The answer depends on the assistant requirements/specification:
  - If it is a purely venue booking system, it should not have answered this question.
  - If it is a headless assistant, and its result should be a completed job, it should 
    probably not answer questions that do not produce artifacts via tool calls (completed 
	booking, generated flyer, etc.). At the same time, if it is a booking assistant that 
	allows for conversation, it may answer the question, because the answer can be part 
	of the booking process (e.g. we need to find venues that are open until the departure 
	of the last train for London tomorrow).
"""

# ── Task D ─────────────────────────────────────────────────────────────────

# Paste the Mermaid output from `python exercise2_langgraph.py task_d` here.
TASK_D_MERMAID_OUTPUT = """
---
config:
  flowchart:
    curve: linear
---
graph TD;
	__start__([<p>__start__</p>]):::first
	agent(agent)
	tools(tools)
	__end__([<p>__end__</p>]):::last
	__start__ --> agent;
	agent -.-> __end__;
	agent -.-> tools;
	tools --> agent;
	classDef default fill:#f2f0ff,line-height:1.2
	classDef first fill-opacity:0
	classDef last fill:#bfb6fc
"""

# Compare the LangGraph graph to exercise3_rasa/data/flows.yml. Min 30 words.
TASK_D_COMPARISON = """
LangGraph is more generic and flexible. Mermaid graph has just 2 key nodes (agent, tools). 
It allows the model to decide the next step at runtime.

Rasa flows.yml is more rigid and predefined. For example, it has specific flows for booking 
confirmation and handling out-of-scope requests. Plus it specifically sets data to be collected 
(guest_count, vegan_count, deposit_amount_gbp) and passed to a further function/tool.

LangGraph should be able to handle more complex scenarios, but it might be less predictable, 
less debuggable, and if some complex scenario fails - it might be more difficult to direct LLM 
in LangGraph how to fix it.
"""

# ── Reflection ─────────────────────────────────────────────────────────────

# The most unexpected thing the agent did. Min 40 words.
# Must reference a specific behaviour from your run.

MOST_SURPRISING = """
The most surprising thing was that the model knew the list of pubs to be checked with 
check_pub_availability() tool after (in Task C) it turned out that the The Bow Bar is full.

I first even thought that I missed some tool which lists all the pubs in Edinburgh.

Later I realized that it took the list from the tool description.
"""