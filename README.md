# MathPix LaTeX Extractor

A Flask web application that converts images containing mathematical equations to LaTeX format using the MathPix API.

## Quick Start

**🚀 Automatic Setup & Run (Recommended):**
```bash
# Linux/macOS
./run

# Windows
run.bat
```

The script will automatically:
- Create virtual environment
- Install dependencies
- Set up environment variables
- Run the application

## Manual Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd images
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` and add your MathPix API credentials:
   - Get your API credentials from [MathPix](https://mathpix.com/)
   - Add your `MATHPIX_APP_ID` and `MATHPIX_APP_KEY`

5. **Run the application**
   ```bash
   python app.py
   ```

## Security Notes

⚠️ **IMPORTANT**: 
- Never commit your `.env` file to version control
- The `.env` file contains sensitive API credentials
- Use `.env.example` as a template for others
- Keep your API keys secure and rotate them regularly

## Usage

1. Open your browser and go to `http://localhost:5000`
2. **Upload an image** containing mathematical equations using one of these methods:
   - **Drag & Drop**: Simply drag an image file onto the upload area
   - **Click to Browse**: Click the upload area or "Choose File" button to select an image
3. The app will automatically detect math content and return the LaTeX representation
4. **Copy the results** using the convenient copy buttons:
   - Copy raw LaTeX code
   - Copy LaTeX with `$$` tags for direct use
   - Copy plain text if no math is detected

## Features

- 🎯 **Drag & Drop Upload** - Simply drag images onto the upload area
- 📋 **One-Click Copy** - Copy LaTeX with or without formatting tags
- 🎨 **Modern UI** - Clean, responsive interface with visual feedback
- 🔍 **Smart Detection** - Separates mathematical LaTeX from plain text
- 🛡️ **File Validation** - Supports PNG, JPG, JPEG, GIF, BMP, WebP (up to 10MB)
- ⚡ **Real-time Feedback** - Visual indicators for drag, drop, and copy operations

```
├── app.py              # Main Flask application
├── templates/
│   └── index.html      # HTML template
├── .env.example        # Environment variables template
├── .env               # Your actual API credentials (not in git)
├── requirements.txt    # Python dependencies
└── README.md          # This file
```
