import os
from notion_client import Client
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

notion = Client(auth=os.getenv("NOTION_API_KEY"))
database_id = os.getenv("NOTION_DATABASE_ID")

def extract_summary_text(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def send_to_notion(summary_file_path):
    today = datetime.now().strftime("%Y-%m-%d")
    summary_content = extract_summary_text(summary_file_path)

    response = notion.pages.create(
        parent={ "database_id": database_id },
        properties={
            "Name": {
                "title": [{
                    "text": {
                        "content": f"GPT Research – {today}"
                    }
                }]
            },
            "Date": {
                "date": {
                    "start": today
                }
            },
            "Summary": {
                "rich_text": [{
                    "text": {
                        "content": summary_content[:2000]
                    }
                }]
            },
            "Raw Markdown": {
                "rich_text": [{
                    "text": {
                        "content": summary_content[:2000]
                    }
                }]
            }
        }
    )
    print("✅ Synced to Notion with page ID:", response["id"])

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 notion_exporter.py path/to/summary.md")
    else:
        send_to_notion(sys.argv[1])
