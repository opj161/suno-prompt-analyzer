#!/usr/bin/env python3

from analyzer import analyze_explorer_styles
from data_loader import load_suno_data
from pathlib import Path

# Load data
DATA_FILE_PATH = Path('data/suno_logic.json')
DEFAULT_STYLES, CO_OCCURRENCE_DATA = load_suno_data(DATA_FILE_PATH)

# Test with negative styles and creative direction
result = analyze_explorer_styles(
    primary_style='rock',
    secondary_style=None,
    negative_prompt_text='pop, electronic',
    creative_direction='Use a guitar solo, theme of rebellion',
    co_occurrence_data=CO_OCCURRENCE_DATA
)

print('CREATIVE BRIEF:')
print(result['creative_brief'])
print('\n' + '='*50 + '\n')

# Test fusion with negative styles and creative direction
result2 = analyze_explorer_styles(
    primary_style='rock',
    secondary_style='jazz',
    negative_prompt_text='pop, country',
    creative_direction='Heavy bass line, urban theme',
    co_occurrence_data=CO_OCCURRENCE_DATA
)

print('FUSION CREATIVE BRIEF:')
print(result2['creative_brief'])
