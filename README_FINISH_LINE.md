# 🏁 Deep Research Workflow – Finish Line Overview

This project represents a complete, production-ready, AI-powered research automation engine. It performs autonomous research, logs outputs, syncs to Notion, pushes to GitHub, and notifies you—all in a single command.

---

## ✅ System Capabilities

| Component | Function |
|----------|----------|
| `deep_research_runner.py` | Executes GPT research prompts |
| `daily_research_prompts.json` | List of prompts for batch processing |
| `flow_auto_runner_full_stack.sh` | Orchestrates full loop (GPT → Notion → GitHub → Notify) |
| `notion_exporter.py` | Sends research summaries to Notion database |
| `push_to_github.sh` | Commits and pushes results to GitHub |
| `store_token_once.sh` | Configures macOS Keychain to store GitHub token |
| `deep_research_cron_setup.sh` | Adds daily cron job at 7:00 AM |
| `deep_research_swiftbar.1m.sh` | One-click SwiftBar trigger |
| `stream_deck_button.json` | Importable config for Stream Deck trigger |
| `notify.sh` | Customizable stub for Slack/email notifications |

---

## 🔐 API & Auth

- `.env` file securely holds:
  - `OPENAI_API_KEY`
  - `NOTION_API_KEY`
  - `NOTION_DATABASE_ID`
- GitHub token is stored using Keychain for repeatable `push`.

---

## 🗃️ Output Structure

Each research run creates:

```
/outputs/YYYY-MM-DD/
├── result_1.md
├── result_2.md
├── summary.md
└── prompts_used.log
```

---

## 🔁 Usage

**Run the full loop manually:**
```bash
./flow_auto_runner_full_stack.sh
```

**Push to GitHub manually:**
```bash
./push_to_github.sh
```

**View logs:**
```bash
cat outputs/YYYY-MM-DD/summary.md
cat outputs/YYYY-MM-DD/prompts_used.log
```

---

## 🚀 Final Status: ✅ COMPLETE – 360° SYSTEM LIVE
You're now running a self-updating intelligence machine from your desktop.
