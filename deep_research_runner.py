import openai
import os
import sys
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def run_deep_research(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You're an expert researcher."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message["content"]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        prompt = sys.argv[1]
        result = run_deep_research(prompt)
        print(result)
    else:
        print("No prompt provided.")
