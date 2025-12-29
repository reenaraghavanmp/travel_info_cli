# Travel Info CLI

A Python command-line tool that generates structured travel information
for a given city and travel purpose (leisure or business).
The tool outputs valid JSON only, suitable for automation and APIs.

This project uses the Google Gemini API via the official google.genai
SDK and loads environment variables using python-dotenv.

---

Features
- Command-line interface (CLI)
- Purpose-aware responses (leisure vs business)
- Strict JSON output format
- Uses Google Gemini API (free tier supported)
- Environment variables loaded securely with .env

---

Technologies Used
- Python 3.10+
- Google Gemini API (google.genai)
- python-dotenv

Key imports used in the project:

from google import genai
from dotenv import load_dotenv

---

Requirements
- Python 3.10 or higher
- Git
- Google Gemini API key

---

Setup Instructions

1. Clone the Repository

git clone https://github.com/yourusername/travel-info-cli.git
cd travel-info-cli

2. Create and Activate a Virtual Environment

macOS / Linux:
python -m venv .venv
source .venv/bin/activate

Windows (PowerShell):
python -m venv .venv
.venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Create .env File

Create a file named .env in the project root:

GOOGLE_API_KEY=your_api_key_here

The API key is loaded in code using:

from dotenv import load_dotenv
load_dotenv()

---

Usage

python travel_info.py "Istanbul" leisure
python travel_info.py "Singapore" business

---

Output Format

The script prints JSON only in the following structure:

{
  "place": "City name",
  "purpose": "leisure or business",
  "overview": [],
  "things_to_know": [],
  "nearby_transport": [],
  "how_to_get_there": "",
  "best_time_to_travel": ""
}

---

Sample Outputs

Sample outputs for different cities and purposes are available in the
samples/ directory.

---

Notes
- Uses Gemini free-tier model (e.g. gemini-1.5-flash)
- Do not commit .env files or API keys
- Ensure .env and .venv/ are added to .gitignore

---

License
This project is intended for educational and demonstration purposes.
