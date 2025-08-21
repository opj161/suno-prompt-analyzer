# suno-prompt-analyzer/data_loader.py

import json
from typing import Tuple, Set, Dict, Any
import streamlit as st

# Use Streamlit's caching to load the data only once.
@st.cache_data
def load_suno_data(path: str) -> Tuple[Set[str], Dict[str, Any]]:
    """
    Loads, parses, and prepares the Suno style data from a JSON file.

    This function is cached, so the data is loaded from disk only once per
    session, ensuring optimal performance.

    Args:
        path: The file path to the suno_logic.json file.

    Returns:
        A tuple containing:
        - A set of all default style strings for fast lookups.
        - A dictionary of the co-occurrence data.
    
    Raises:
        FileNotFoundError: If the file at the specified path does not exist.
        ValueError: If the file is not a valid JSON or lacks expected keys.
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # For fast keyword checking (O(1) average time complexity)
        default_styles_set = set(data["default_styles"])
        co_occurrence_dict = data["co_existing_styles_dict"]

        if not default_styles_set or not co_occurrence_dict:
            raise ValueError("JSON file is missing 'default_styles' or 'co_existing_styles_dict' keys.")

        return default_styles_set, co_occurrence_dict

    except FileNotFoundError:
        st.error(f"FATAL: Data file not found at '{path}'. Please make sure 'suno_logic.json' is in the 'data' subfolder.")
        st.stop()
    except (json.JSONDecodeError, KeyError) as e:
        st.error(f"FATAL: Error parsing the data file '{path}'. It may be corrupted or not valid JSON. Details: {e}")
        st.stop()