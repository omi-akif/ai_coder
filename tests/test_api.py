"""
Test script for the AI Coder API
"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_health_check():
    """Test the root health check endpoint"""
    response = requests.get(f"{BASE_URL}/")
    print("Health Check Response:")
    print(json.dumps(response.json(), indent=2))
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    print("✓ Health check passed\n")

def test_generate_code():
    """Test code generation endpoint"""
    payload = {
        "topic": "Python Calculator",
        "requirements": "Create a simple calculator class with add, subtract, multiply, and divide methods"
    }
    
    print("Sending code generation request...")
    print(f"Topic: {payload['topic']}")
    print(f"Requirements: {payload['requirements']}")
    print("\nWaiting for response (this may take a while)...\n")
    
    response = requests.post(f"{BASE_URL}/generate-code", json=payload)
    
    print("Response Status:", response.status_code)
    result = response.json()
    
    if result["success"]:
        print("\n✓ Code generation successful!")
        print("\nGenerated Code:")
        print("=" * 80)
        print(result["result"])
        print("=" * 80)
    else:
        print("\n✗ Code generation failed!")
        print(f"Error: {result['error']}")

if __name__ == "__main__":
    try:
        print("Testing AI Coder API")
        print("=" * 80)
        test_health_check()
        test_generate_code()
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API server.")
        print("Make sure the server is running with: conda run -n coder_agent api_server")
    except Exception as e:
        print(f"Error during testing: {e}")
