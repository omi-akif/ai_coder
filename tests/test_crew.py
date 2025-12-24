#!/usr/bin/env python3
"""
Simple test script to verify the crew works with Ollama.
"""
import sys
from ai_coder.crew import AiCoder

def test_crew():
    """Test the crew with a simple coding task."""
    inputs = {
        'topic': 'Python Hello World',
        'requirements': 'Create a simple hello world Python script'
    }
    
    print("Starting test of the coding agent...")
    print(f"Topic: {inputs['topic']}")
    print(f"Requirements: {inputs['requirements']}")
    print("-" * 50)
    
    try:
        result = AiCoder().crew().kickoff(inputs=inputs)
        print("\n" + "=" * 50)
        print("SUCCESS! The crew completed the task.")
        print("=" * 50)
        return 0
    except Exception as e:
        print(f"\nERROR: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(test_crew())
