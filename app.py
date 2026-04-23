from agent.intent import detect_intent
from agent.rag import retrieve_answer
from agent.tools import mock_lead_capture
from agent.state import AgentState

state = AgentState()

print("🤖 AutoStream Agent Started!")

while True:
    user_input = input("\nYou: ")

    # If already collecting details → continue flow
    if state.collecting:
        if not state.name:
            state.name = user_input
            print("Bot: Your email?")
            continue

        elif not state.email:
            state.email = user_input
            print("Bot: Which platform do you create on?")
            continue

        elif not state.platform:
            state.platform = user_input

            mock_lead_capture(state.name, state.email, state.platform)

            print("Bot: Thank you! Our team will contact you soon.")

            state.lead_complete = True
            state.collecting = False
            continue

    intent = detect_intent(user_input)

    # Greeting
    if intent == "greeting":
        print("Bot: Hey! How can I help you today?")

    # Product Query
    elif intent == "product_query":
        response = retrieve_answer(user_input)
        print(f"Bot: {response}")

    # High Intent
    elif intent == "high_intent":
        if state.lead_complete:
            print("Bot: You've already signed up! We'll contact you soon 😊")
        else:
            print("Bot: Awesome! Let's get you started 🚀")
            print("Bot: What's your name?")
            state.collecting = True

    else:
        print("Bot: Sorry, I didn’t understand that.")