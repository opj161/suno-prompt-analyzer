# Test script to verify Gemini API functionality directly
import os
from analyzer import generate_polished_prompt_with_gemini

def test_gemini_direct():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("ERROR: GEMINI_API_KEY not found in environment variables")
        return
    
    test_brief = """
    Primary Style: Folk
    Secondary Style: Acoustic
    Creative Direction: Create a melancholic ballad about lost love
    """
    
    print("Testing Gemini API call...")
    result = generate_polished_prompt_with_gemini(test_brief, api_key)
    
    print(f"Result type: {type(result)}")
    print(f"Result length: {len(result) if result else 0}")
    print(f"Result starts with ERROR: {result.startswith('ERROR:') if result else 'N/A'}")
    print(f"First 200 chars: {result[:200] if result else 'None'}")
    
    return result

if __name__ == "__main__":
    test_gemini_direct()
