#!/usr/bin/env python3

# Test script to create sample responses for testing the UI

from app import app
import json

def test_ui():
    """Test the UI with different response types"""
    
    with app.test_client() as client:
        print("Testing UI with different response scenarios...")
        
        # Test case 1: LaTeX response
        print("\n1. Testing LaTeX response...")
        latex_response = {
            "latex": "x^2 + y^2 = 1",
            "text": None,
            "error": None,
            "full_response": None
        }
        
        # Test case 2: Text response  
        print("2. Testing Text response...")
        text_response = {
            "latex": None,
            "text": "This is plain text without mathematical equations",
            "error": None,
            "full_response": None
        }
        
        # Test case 3: Error response
        print("3. Testing Error response...")
        error_response = {
            "latex": None,
            "text": None,
            "error": "API rate limit exceeded",
            "full_response": None
        }
        
        print("✅ All test cases defined. Upload different types of images to test!")

if __name__ == "__main__":
    test_ui()
