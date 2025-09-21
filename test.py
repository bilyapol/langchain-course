# test_env.py (or add to hello.py)
import os

from dotenv import load_dotenv

load_dotenv()  # Loads .env from current directory (project root)

print("OPENAI_API_KEY =", os.getenv("OPENAI_API_KEY"))
print("LANGCHAIN_API_KEY =", os.getenv("LANGCHAIN_API_KEY"))
print("HUGGINGFACEHUB_API_TOKEN =", os.getenv("HUGGINGFACEHUB_API_TOKEN"))
