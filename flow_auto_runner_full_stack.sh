#!/bin/bash

echo "🧠 Starting Full Stack Deep Research Workflow"

TODAY=$(date '+%Y-%m-%d')
OUTPUT_DIR="outputs/$TODAY"
mkdir -p "$OUTPUT_DIR"

PROMPT_FILE="daily_research_prompts.json"
if [ ! -f "$PROMPT_FILE" ]; then
  echo "❌ Missing $PROMPT_FILE"
  exit 1
fi

index=1
for prompt in $(jq -r '.[]' "$PROMPT_FILE"); do
  echo "🔍 Running prompt #$index"
  python3 deep_research_runner.py "$prompt" > "$OUTPUT_DIR/result_$index.md"
  echo "$prompt" >> "$OUTPUT_DIR/prompts_used.log"
  ((index++))
done

echo "📚 Compiling summary..."
echo "📚 GPT Summary for $TODAY" > "$OUTPUT_DIR/summary.md"
for f in $OUTPUT_DIR/result_*.md; do
  echo "------------------------------" >> "$OUTPUT_DIR/summary.md"
  cat "$f" >> "$OUTPUT_DIR/summary.md"
done

echo "📤 Sending to Notion..."
python3 notion_exporter.py "$OUTPUT_DIR/summary.md"

echo "📦 Pushing results to GitHub..."
git add .
git commit -m "Auto-push: Deep Research Results for $TODAY"
git push

echo "🔔 Triggering notification..."
bash notify.sh "Deep Research Complete for $TODAY"

echo "✅ All tasks complete."
