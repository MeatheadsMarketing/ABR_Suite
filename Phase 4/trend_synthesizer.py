import os
from datetime import datetime
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def load_latest_summary(base_dir="outputs"):
    all_folders = sorted([
        d for d in os.listdir(base_dir)
        if os.path.isdir(os.path.join(base_dir, d))
    ], reverse=True)
    if not all_folders:
        raise FileNotFoundError("No output folders found.")
    latest = all_folders[0]
    summary_path = os.path.join(base_dir, latest, "summary.md")
    if not os.path.exists(summary_path):
        raise FileNotFoundError(f"summary.md not found in {latest}")
    with open(summary_path, "r") as f:
        return f.read(), latest

def extract_trends(summary_text):
    prompt = f"""
You are a trend analyst assistant. Based on the following GPT research summary, extract:
1. Top 5–10 emerging trends, technologies, ideas, or opportunities.
2. Organize them by category or theme if possible.
3. Include 3 recommended follow-up questions or prompts for deeper exploration.

Summary:
"""
{summary_text}
"""
Now generate the analysis:
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a trend analyzer."},
            {"role": "user", "content": prompt}
        ]
    )
    return response["choices"][0]["message"]["content"]

def write_trend_report(trends, date_tag):
    output_path = f"outputs/{date_tag}/trend_report.md"
    with open(output_path, "w") as f:
        f.write("# 🔍 Trend Synthesis Report\n\n")
        f.write(trends)
    print(f"✅ Trend report written to {output_path}")

if __name__ == "__main__":
    try:
        summary, folder = load_latest_summary()
        trends = extract_trends(summary)
        write_trend_report(trends, folder)
    except Exception as e:
        print(f"❌ Error: {e}")
