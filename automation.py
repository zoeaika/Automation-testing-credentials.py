import streamlit as st
from operator import itemgetter

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

# AI-Suggested Implementation
def sort_dict_list_ai(dict_list, key):
    """
    Sort a list of dictionaries by a specified key using itemgetter for efficiency.
    Args:
        dict_list: List of dictionaries
        key: Key to sort by
    Returns:
        Sorted list of dictionaries
    """
    return sorted(dict_list, key=itemgetter(key))

# Example data
data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

# Streamlit UI
st.title("Dictionary List Sorter")
st.subheader("Example Data:")
st.write(data)

# User controls
col1, col2 = st.columns(2)
sort_key = col1.selectbox("Sort Key", options=["name", "age"])
sort_method = col2.radio("Sort Method", options=["Manual (Lambda)", "AI (Itemgetter)"])

# Sorting execution
if sort_method == "Manual (Lambda)":
    result = sort_dict_list_manual(data, sort_key)
else:
    result = sort_dict_list_ai(data, sort_key)

# Display results
st.subheader("Sorted Result:")
st.write(result)

# Debug info
st.caption(f"Sorted by: {sort_key} | Method: {sort_method}")
