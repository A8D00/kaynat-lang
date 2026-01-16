def suggest(keyword):
    suggestions = {
        "كيان": ["قرار", "الحالة"],
        "قرار": ["شرط", "تحول"]
    }
    return suggestions.get(keyword, [])
