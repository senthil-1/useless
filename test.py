import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("❌ API key not found in .env")
    exit()

client = OpenAI(api_key=api_key)

try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # You can switch to gpt-4o or gpt-4-turbo
        messages=[
            {"role": "system", "content": "You are a friendly AI that talks about fridges."},
            {"role": "user", "content": "Describe the mood of a fridge with expired milk and chocolate."}
        ]
    )

    print("✅ API call successful!")
    print("AI replied:", response.choices[0].message["content"])

except Exception as e:
    print("❌ API call failed:", e)
