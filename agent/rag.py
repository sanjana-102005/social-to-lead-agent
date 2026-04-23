import json

# Load knowledge base
def load_knowledge():
    with open("data/knowledge_base.json", "r") as f:
        return json.load(f)


# Retrieve answer based on user query
def retrieve_answer(user_query):
    kb = load_knowledge()
    query = user_query.lower()

    # Pricing related (more flexible now)
    if any(word in query for word in ["price", "pricing", "plan", "cost"]):
        basic = kb["pricing"]["basic"]
        pro = kb["pricing"]["pro"]

        return f"""
Here are our plans:

Basic Plan:
Price: {basic['price']}
Features: {', '.join(basic['features'])}

Pro Plan:
Price: {pro['price']}
Features: {', '.join(pro['features'])}
"""

    # Refund policy
    elif any(word in query for word in ["refund", "money back"]):
        return kb["policies"]["refund"]

    # Support policy
    elif any(word in query for word in ["support", "help"]):
        return kb["policies"]["support"]

    # Default fallback
    else:
        return "Sorry, I couldn't find that info."