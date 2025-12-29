import os
# import google.generativeai as genai
from google import genai
from dotenv import load_dotenv # Correct way
load_dotenv()


# Access the variables
api_key = os.getenv("GOOGLE_API_KEY")
print(f"My API Key is: {api_key}")



def connect_gemini():
    client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

    model = "gemini-2.5-flash-lite"  # free tier model
    client.models.generate_content(model=model, contents="ping")

    print("Connected to Gemini (free tier)")

if __name__ == "__main__":
    connect_gemini()