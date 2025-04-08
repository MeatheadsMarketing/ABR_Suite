import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_competitors(summary):
    prompt = f"""From the following summary, identify any competitor names and their activities.\n\n{summary}"""
    return openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )["choices"][0]["message"]["content"]
