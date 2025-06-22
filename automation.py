# Manual Implementation
def sort_dict_list_manual(dict_list, key):
    """
    Sort a list of dictionaries by a specified key.
    Args:
        dict_list: List of dictionaries
        key: Key to sort by
    Returns:
        Sorted list of dictionaries
    """
    return sorted(dict_list, key=lambda x: x[key])

# AI-Suggested Implementation (simulated Copilot suggestion)
def sort_dict_list_ai(dict_list, key):
    """
    Sort a list of dictionaries by a specified key using itemgetter for efficiency.
    Args:
        dict_list: List of dictionaries
        key: Key to sort by
    Returns:
        Sorted list of dictionaries
    """
    from operator import itemgetter
    return sorted(dict_list, key=itemgetter(key))

# Example usage
data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

# Test both functions
sorted_manual = sort_dict_list_manual(data, "age")
sorted_ai = sort_dict_list_ai(data, "age")
print("Sorted Manually:", sorted_manual)
print("Sorted with AI:", sorted_ai)
 
