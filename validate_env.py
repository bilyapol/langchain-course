import os

from dotenv import load_dotenv

load_dotenv()

REQUIRED_KEYS = [
    "OPENAI_API_KEY",
    "LANGCHAIN_API_KEY",
    "HUGGINGFACEHUB_API_TOKEN",
]

print("🔍 Validating environment variables...\n")

for key in REQUIRED_KEYS:
    value = os.getenv(key)
    if value is None or value.strip() == "":
        print(f"❌ {key} is missing or empty!")
    else:
        print(f"✅ {key} = {value[:15]}...")  # Show first 15 chars for safety
