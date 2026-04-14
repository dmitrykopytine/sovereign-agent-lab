"""
Exercise 3 — Answers
====================
Fill this in after completing the three Rasa conversations.

CALM vs Old Rasa — what changed
---------------------------------
The old open-source Rasa approach used:
  - nlu.yml: intent training examples
  - rules.yml: explicit dialogue rules
  - FormValidationAction: Python class to parse slot values

Rasa Pro CALM uses:
  - flows.yml: natural language descriptions of what each flow does
  - from_llm slots: the LLM extracts values from conversation
  - ONE custom action: ActionValidateBooking for the business rules

The conversation is the same from the manager's perspective.
The machinery underneath is completely different.

CONVERSATION SCRIPTS
---------------------
Conversation 1 (happy path):
  You:    calling to confirm a booking
  Agent:  [asks guest count]
  You:    160 guests
  Agent:  [asks vegan count]
  You:    about 50 need vegan
  Agent:  [asks deposit]
  You:    £200 deposit
  Agent:  [confirms or escalates?]

Conversation 2 (deposit too high):
  Same as above but use a deposit above £300 (e.g. "£500 deposit").

Conversation 3 (out of scope):
  Start normally, then when asked for vegan count say something like
  "can you arrange parking for the speakers?" and observe what happens.
  Does CALM handle this differently than the old rules approach?
"""

# ── Conversation 1: Happy path ─────────────────────────────────────────────

CONVERSATION_1_TRACE = """
Your input ->  calling to confirm a booking                                                                       
How many guests are you confirming for tonight's event?
Your input ->  160 guests                                                                                         
And how many of those guests will need vegan meals?
Your input ->  about 50 need vegan                                                                                
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  £200 deposit                                                                                       
Thank you — booking confirmed. 160 guests, 50 requiring vegan meals, £200 deposit accepted. I'll send written confirmation to the organiser shortly.
Is there anything else I can help you with?
"""

CONVERSATION_1_OUTCOME = "confirmed"   # "confirmed" or "escalated"

# ── Conversation 2: Deposit too high ───────────────────────────────────────

CONVERSATION_2_TRACE = """
Your input ->  calling to confirm a booking                                                                       
How many guests are you confirming for tonight's event?
Your input ->  160 guests                                                                                         
And how many of those guests will need vegan meals?
Your input ->  about 50 need vegan                                                                                
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  £500 deposit                                                                                       
I need to check one thing with the organiser before I can confirm. The issue is: a deposit of £500 exceeds the organiser's authorised limit of £300. Can I call you back within 15 minutes?
Is there anything else I can help you with?
"""

CONVERSATION_2_OUTCOME = "escalated"   # "confirmed" or "escalated"
CONVERSATION_2_REASON  = "a deposit of £500 exceeds the organiser's authorised limit of £300"   # the reason the agent gave for escalating

# ── Conversation 3: Out of scope ───────────────────────────────────────────

CONVERSATION_3_TRACE = """
Your input ->  calling to confirm a booking                                                                       
How many guests are you confirming for tonight's event?
Your input ->  160 guests                                                                                         
And how many of those guests will need vegan meals?
Your input ->  can you arrange parking for the speakers?                                                          
I'm sorry, I'm not trained to help with that.
And how many of those guests will need vegan meals?
Your input ->  
"""

# Describe what CALM did after the out-of-scope message. Min 20 words.
CONVERSATION_3_WHAT_HAPPENED = """
The agent returned the message "I'm sorry, I'm not trained to help with that."
Then it returned to the last non-answered question and asked it again.
"""

# Compare Rasa CALM's handling of the out-of-scope request to what
# LangGraph did in Exercise 2 Scenario 3. Min 40 words.
OUT_OF_SCOPE_COMPARISON = """
Rasa CALM handled the out-of-scope request by responding with a predefined message 
"I'm sorry, I'm not trained to help with that.".

LangGraph answered to a non-domain question, which was not suitable in the context 
of the task being solved - booking a venue (but honestly in the case of LangGraph we 
did not provide instructions to the LLM what is out-of-scope and how to handle it).
"""

# ── Task B: Cutoff guard ───────────────────────────────────────────────────

TASK_B_DONE = True   # True or False

# List every file you changed.
TASK_B_FILES_CHANGED = ["exercise3_rasa/actions/actions.py"]

# How did you test that it works? Min 20 words.
TASK_B_HOW_YOU_TESTED = """
I set the time condition to True, retrained rasa and ran the conversation. The agent 
asked all the questions and then escalated and returned the message "I need to check 
one thing with the organiser before I can confirm. The issue is: it is past 16:45 — 
insufficient time to process the confirmation before the 5 PM deadline. Can I call 
you back within 15 minutes?"
"""

# ── CALM vs Old Rasa ───────────────────────────────────────────────────────

# In the old open-source Rasa (3.6.x), you needed:
#   ValidateBookingConfirmationForm with regex to parse "about 160" → 160.0
#   nlu.yml intent examples to classify "I'm calling to confirm"
#   rules.yml to define every dialogue path
#
# In Rasa Pro CALM, you need:
#   flow descriptions so the LLM knows when to trigger confirm_booking
#   from_llm slot mappings so the LLM extracts values from natural speech
#   ONE action class (ActionValidateBooking) for the business rules
#
# What does this simplification cost? What does it gain?
# Min 30 words.

CALM_VS_OLD_RASA = """
LLM handles the language understanding in CALM. Python handles the business rules.

New approach can handle natural speech better (for example, I can even answer 
'40 + 4 speakers' and it will understand that it's 44 people - such things cannot be 
reliably handled by regular expressions).

Old approach is less risky and 100% predictable. LLM can hallucinate and make mistakes. 
LLM may introduce security issues (for example, disclose internal information if used 
incorrectly/unsafely).
"""

# ── The setup cost ─────────────────────────────────────────────────────────

# CALM still required: config.yml, domain.yml, flows.yml, endpoints.yml,
# rasa train, two terminals, and a Rasa Pro licence.
# The old Rasa ALSO needed nlu.yml, rules.yml, and a FormValidationAction.
#
# CALM is simpler. But it's still significantly more setup than LangGraph.
# That setup bought you something specific.
# Min 40 words.

SETUP_COST_VALUE = """
Rasa CALM is better (compared to LangGraph) because:
  - it is more algorithmic and predictable compared to LangGraph.
  - it is guaranteed to ask questions which are important for the business logic 
    (e.g. vegan_count, deposit_amount_gbp).
  - it calls predefined tools, without skipping/forgetting/guessing/hallucinating 
    input parameters.
  - it produces very predictable configurable responses.
  - it, generally, has potentially less security issues compared to LangGraph.
"""
