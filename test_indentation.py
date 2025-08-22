#!/usr/bin/env python3
"""Test script to verify all indentation is correct."""

from analyzer import analyze_explorer_styles
from data_loader import load_suno_data
from pathlib import Path

def test_indentation():
    # Load test data
    data_file = Path('data/suno_logic.json')
    default_styles, co_occurrence_data = load_suno_data(data_file)
    
    # Test single style analysis
    result = analyze_explorer_styles('rock', None, co_occurrence_data)
    print('Single style analysis successful')
    print('Keys in result:', list(result.keys()))
    
    # Test fusion analysis
    result = analyze_explorer_styles('rock', 'pop', co_occurrence_data)
    print('Fusion analysis successful')
    print('Keys in result:', list(result.keys()))
    
    print('All indentation tests passed!')

if __name__ == '__main__':
    test_indentation()
