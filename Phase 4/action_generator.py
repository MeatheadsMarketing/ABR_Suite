import os
from datetime import datetime
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def load_all_sources(base_dir="outputs"):
    folders = sorted([
        d for d in os.listdir(base_dir)
        if os.path.isdir(os.path.join(base_dir, d))
    ], reverse=True)
    if not folders:
        raise FileNotFoundError("No output folders found.")
    latest = folders[0]
    folder_path = os.path.join(base_dir, latest)

    def read_file(name):
        path = os.path.join(folder_path, name)
        return open(path).read() if os.path.exists(path) else ""

    return {
        "folder": latest,
        "summary": read_file("summary.md"),
        "trends": read_file("trend_report.md"),
        "competitors": read_file("competitor_report.md")
    }

def generate_actions(summary, trends, competitors):
    prompt = f"""
You are a strategic action planner.

Based on the following inputs:
1. Research Summary
2. Trends Identified
3. Competitor Activity

Generate:
- 5 to 7 concrete strategic actions
- Label each with an urgency level: HIGH / MEDIUM / LOW
- Optionally include 1-2 recommended GPT research prompts

== RESEARCH SUMMARY ==
{summary}

== TRENDS ==
{trends}

== COMPETITORS ==
{competitors}

Now synthesize actionable steps:
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a business strategist AI."},
            {"role": "user", "content": prompt}
        ]
    )
    return response["choices"][0]["message"]["content"]

def write_action_plan(output, folder):
    path = f"outputs/{folder}/action_plan.md"
    with open(path, "w") as f:
        f.write("# 🎯 Action Plan Based on Strategic Insights\n\n")
        f.write(output)
    print(f"✅ Action plan saved to {path}")

if __name__ == "__main__":
    try:
        data = load_all_sources()
        actions = generate_actions(data["summary"], data["trends"], data["competitors"])
        write_action_plan(actions, data["folder"])
    except Exception as e:
        print(f"❌ Error: {e}")
