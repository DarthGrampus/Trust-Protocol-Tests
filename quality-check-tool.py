def check_quality(answer_text):
    # Simple word count for depth (higher = better layers of ideas)
    words = len(answer_text.split())
    excitement_words = ['amazing', 'spark', 'magic', 'unravel']  # Counts fun energy
    excitement_count = sum(1 for word in excitement_words if word in answer_text.lower())
    yes_words = ['yes', 'agree', 'perfect']  # Counts blind agreement (should be low)
    yes_count = sum(1 for word in yes_words if word in answer_text.lower())
    return {"depth": words, "energy": excitement_count, "agreement": yes_count}

# Example:
result = check_quality("Your AI answer here")
print(result)
