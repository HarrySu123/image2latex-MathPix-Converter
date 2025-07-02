#!/usr/bin/env python3

import os
import requests
import base64
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

MATHPIX_APP_ID = os.getenv("MATHPIX_APP_ID")
MATHPIX_APP_KEY = os.getenv("MATHPIX_APP_KEY")

print(f"App ID: {MATHPIX_APP_ID}")
print(f"App Key: {MATHPIX_APP_KEY[:10]}..." if MATHPIX_APP_KEY else "No API Key found")

if not MATHPIX_APP_ID or not MATHPIX_APP_KEY:
    print("ERROR: Missing API credentials!")
    exit(1)

headers = {
    "app_id": MATHPIX_APP_ID,
    "app_key": MATHPIX_APP_KEY,
    "Content-type": "application/json"
}

# Create a minimal test image (1x1 pixel PNG)
test_image_b64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8/5+hHgAHggJ/PchI7wAAAABJRU5ErkJggg=="

print("\nTesting MathPix API...")
print(f"API URL: https://api.mathpix.com/v3/text")

response = requests.post("https://api.mathpix.com/v3/text", headers=headers, json={
    "src": f"data:image/png;base64,{test_image_b64}",
    "formats": ["latex_simplified"]
})

print(f"\nStatus Code: {response.status_code}")
print(f"Response Headers: {dict(response.headers)}")
print(f"Response Body: {response.text}")

if response.status_code == 200:
    result = response.json()
    print(f"\nParsed JSON: {result}")
else:
    print(f"\nError: {response.status_code} - {response.text}")
