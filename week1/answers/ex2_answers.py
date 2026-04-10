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

TASK_A_TOOLS_CALLED = ["check_pub_availability", "check_pub_availability", "get_edinburgh_weather", "calculate_catering_cost", "generate_event_flyer"]

# Which venue did the agent confirm? Must be one of:
# "The Albanach", "The Haymarket Vaults", or "none"
TASK_A_CONFIRMED_VENUE = "The Albanach"

# Total catering cost the agent calculated. Float, e.g. 5600.0
# Write 0.0 if the agent didn't calculate it.
TASK_A_CATERING_COST_GBP = 5600.0

# Did the weather tool return outdoor_ok = True or False?
TASK_A_OUTDOOR_OK = False

TASK_A_NOTES = "Agent was not making a proper tool call. I had to fix the code to make it work."   # optional — anything unexpected

# ── Task B ─────────────────────────────────────────────────────────────────

# Has generate_event_flyer been implemented (not just the stub)?
TASK_B_IMPLEMENTED = True   # True or False

# The image URL returned (or the error message if still a stub).
TASK_B_IMAGE_URL_OR_ERROR = "https://pictures-storage.storage.eu-north1.nebius.cloud/text2img-ab8ccf9f-43e8-47ff-803d-f1617db2a585_00001_.webp"

# The prompt sent to the image model. Copy from terminal output.
TASK_B_PROMPT_USED = "Professional event flyer for Edinburgh AI Meetup, tech professionals, modern venue at The Haymarket Vaults, Edinburgh. 160 guests tonight. Warm lighting, Scottish architecture background, clean modern typography."

# ── Task C ─────────────────────────────────────────────────────────────────

# Scenario 1: first choice unavailable
# Quote the specific message where the agent changed course. Min 20 words.
SCENARIO_1_PIVOT_MOMENT = """
The agent launched check_pub_availability() for The Bow Bar first, and it returned meets_all_constraints=false.
Then it checked all other known venues since they all are mentioned in the check_pub_availability tool description.
Based on the 2 positive result (The Haymarket Vaults and The Albanach), it chose The Albanach as the venue.

[TOOL_CALL] → check_pub_availability({"pub_name": "The Bow Bar", "required_capacity": "160", "requires_vegan": "true")
[TOOL]
{"success": true, "pub_name": "The Bow Bar", "address": "80 West Bow, Edinburgh", "capacity": 80, "vegan": true, "status": "full", "meets_all_constraints": false}
"""

SCENARIO_1_FALLBACK_VENUE = "The Albanach"

# Scenario 2: impossible constraint (300 guests)
# Did the agent recommend a pub name not in the known venues list?
SCENARIO_2_HALLUCINATED = False   # True or False

# Paste the final [AI] message.
SCENARIO_2_FINAL_ANSWER = """
None of the known venues meet the capacity and dietary requirements. The Albanach, The Haymarket Vaults, and The Guilford Arms have a capacity of 180, 160, and 200 respectively, which is less than the required capacity of 300. The Bow Bar has a capacity of 80, which is also less than the required capacity, and it is currently full. Therefore, none of the known venues can accommodate 300 people with vegan options.
"""

# Scenario 3: out of scope (train times)
# Did the agent try to call a tool?
SCENARIO_3_TRIED_A_TOOL = False   # True or False

SCENARIO_3_RESPONSE = """
I'm not able to provide real-time information or specific details about train schedules. However, I can suggest some options to help you find the information you're looking for:

1. Check the National Rail website or mobile app for the latest train schedules and fares.
2. Contact the National Rail Enquiries helpline on 03457 48 49 50 for assistance with planning your journey.
3. Visit the ScotRail website or mobile app for information on trains from Edinburgh Waverley to London.

Please note tha...
"""

# Would this behaviour be acceptable in a real booking assistant? Min 30 words.
SCENARIO_3_ACCEPTABLE = """
The answer depends on the assistant requirements/specification.
If it is a purely venue booking system, it should not answer this question.
If it is a headless assistant, and its result should be a completed job, it should probably not answer questions that do not produce artifacts via tool calls (completed booking, generated flyer, etc.).
At the same time, if it is a booking assistant that allows for conversation, it may answer the question, because the answer can be part of the booking process (e.g. we need to find venues that are open until the departure of the last train for London tonight).
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

# Compare the LangGraph graph to exercise3_rasa/data/rules.yml. Min 30 words.
TASK_D_COMPARISON = """
LangGraph is more generic and flexible. Mermaid graph has just 2 key nodes (agent, tools). It allows the model to decide the next step at runtime.
Rasa flows.yml is more rigid and predefined. For example, it has specific flows for booking confirmation and handling out-of-scope requests. Plus it specifically sets data to be collected (guest_count, vegan_count, deposit_amount_gbp) and passed to a further function/tool.
LangGraph should be able to handle more complex scenarios, but it might be less predictable, less debuggable, and if some complex scenario fails - it might be more difficult to direct LLM in LangGraph how to fix it.
"""

# ── Reflection ─────────────────────────────────────────────────────────────

# The most unexpected thing the agent did. Min 40 words.
# Must reference a specific behaviour from your run.

MOST_SURPRISING = """
The most surprising thing was that the model knew the list of pubs to be checked with check_pub_availability() tool after (in Task A) it turned out that the The Bow Bar is full.
I first even thought that I missed some tool which lists all the pubs in Edinburgh.
Later I realized that it took the list from the tool description.
"""
