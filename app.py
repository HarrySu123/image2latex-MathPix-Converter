import os
import base64
import requests
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.exceptions import RequestEntityTooLarge
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10MB max file size

MATHPIX_APP_ID = os.getenv("MATHPIX_APP_ID")
MATHPIX_APP_KEY = os.getenv("MATHPIX_APP_KEY")
HEADERS = {
    "app_id": MATHPIX_APP_ID,
    "app_key": MATHPIX_APP_KEY,
    "Content-type": "application/json"
}

MATHPIX_API_URL = "https://api.mathpix.com/v3/text"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("image")
        if file and file.filename:
            # Check file size (additional server-side validation)
            if len(file.read()) > 10 * 1024 * 1024:  # 10MB
                return render_template("index.html", error="File size must be less than 10MB")
            
            file.seek(0)  # Reset file pointer after reading for size check
            
            # Get the file extension to set correct MIME type
            filename = file.filename.lower()
            if filename.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')):
                if filename.endswith('.png'):
                    mime_type = "image/png"
                elif filename.endswith(('.jpg', '.jpeg')):
                    mime_type = "image/jpeg"
                elif filename.endswith('.gif'):
                    mime_type = "image/gif"
                elif filename.endswith('.bmp'):
                    mime_type = "image/bmp"
                elif filename.endswith('.webp'):
                    mime_type = "image/webp"
            else:
                return render_template("index.html", error="Please upload a valid image file (PNG, JPG, JPEG, GIF, BMP, WebP)")
            
            image_data = base64.b64encode(file.read()).decode()
            
            # Debug: Print API credentials (first few chars only)
            print(f"API ID: {MATHPIX_APP_ID[:10]}...")
            print(f"API Key: {MATHPIX_APP_KEY[:10]}...")
            
            response = requests.post(MATHPIX_API_URL, headers=HEADERS, json={
                "src": f"data:{mime_type};base64,{image_data}",
                "formats": ["latex_simplified"]
            })
            
            # Debug: Print response details
            print(f"Response Status: {response.status_code}")
            print(f"Response Headers: {response.headers}")
            print(f"Response Content: {response.text}")
            
            if response.status_code != 200:
                return render_template("index.html", error=f"API Error: {response.status_code} - {response.text}")
            
            result = response.json()
            latex = result.get("latex_simplified", "")
            text_found = result.get("text", "")
            error_msg = result.get("error", "")
            
            # Determine the type of response
            response_data = {
                "latex": latex,
                "text": text_found,
                "error": error_msg,
                "full_response": result if not latex and not text_found and not error_msg else None
            }
            
            return render_template("index.html", **response_data)
    return render_template("index.html")

@app.errorhandler(RequestEntityTooLarge)
def handle_file_too_large(e):
    return render_template("index.html", error="File too large! Please upload an image smaller than 10MB"), 413

if __name__ == "__main__":
    app.run(debug=True)
