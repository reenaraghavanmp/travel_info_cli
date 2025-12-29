import sys
import json
import os
from google import genai
from google.genai.errors import ClientError
from dotenv import load_dotenv
load_dotenv()

def build_prompt(place: str, purpose: str) -> str:
    return f"""
You are a travel information generator.

Generate travel information for the place "{place}" with the purpose "{purpose}".

Rules (must follow strictly):
- Output MUST be valid JSON only.
- No extra text outside JSON
- Overview must contain 3 to 5 concise bullet points, Tailor content to the given purpose (leisure vs business).

Required JSON structure:
{{
  "place": "{place}",
  "purpose": "{purpose}",
  "overview": [],
  "things_to_know": [],
  "nearby_transport": [],
  "how_to_get_there": "",
  "best_time_to_travel": ""
}}
""".strip()

def main():
    if len(sys.argv) != 3:
        print(json.dumps({
            "error": "Usage: python travel_info.py \"Place\" <leisure|business>"
        }))
        sys.exit(1)

    place = sys.argv[1]
    purpose = sys.argv[2].lower()

    if purpose not in {"leisure", "business"}:
        print(json.dumps({
            "error": "Purpose must be either 'leisure' or 'business'"
        }))
        sys.exit(1)

    client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=build_prompt(place, purpose)
        )

        # Print ONLY the JSON returned by the model
        print(response.text)

    except ClientError as e:
        print(json.dumps({
            "error": "Gemini API error",
            "details": str(e)
        }))

if __name__ == "__main__":
    main()
    