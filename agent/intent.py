def detect_intent(user_input):
    import difflib

    text = user_input.lower()

    # Helper: fuzzy match
    def similar(word, keywords):
        return any(difflib.get_close_matches(word, keywords, n=1, cutoff=0.7))

    words = text.split()

    # Greeting
    if any(similar(word, ["hi", "hello", "hey"]) for word in words):
        return "greeting"

    # High intent
    action_words = ["buy", "subscribe", "get", "start", "take", "want", "need", "try", "give"]
    plan_words = ["pro", "plan", "subscription"]

    if any(similar(word, action_words) for word in words) and any(similar(word, plan_words) for word in words):
        return "high_intent"

    # Product query
    product_words = ["price", "pricing", "cost", "features", "plans"]

    if any(similar(word, product_words) for word in words):
        return "product_query"

    return "unknown"