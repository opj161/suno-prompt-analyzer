from analyzer import analyze_explorer_styles
from data_loader import load_suno_data
from pathlib import Path
import traceback

# Load data
data_file = Path('data/suno_logic.json')
default_styles, co_occurrence_data = load_suno_data(data_file)

# Test with a common style
try:
    result = analyze_explorer_styles('rock', None, co_occurrence_data)
    print('Success: rock analysis worked')
    if 'error' in result:
        print('ERROR found in result:', result['error'])
    else:
        print('No errors in result')
        print('Keys in result:', list(result.keys()))
except Exception as e:
    print('Exception occurred:', str(e))
    traceback.print_exc()
