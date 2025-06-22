pip install streamlit
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
    Sort a list of dictionaries by a specified key us
