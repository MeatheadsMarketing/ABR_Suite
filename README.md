# 🔍 Modular Research Suite (ABR_Suite)

A fully autonomous, multi-phase assistant framework for GPT-powered strategic research, deployed via Streamlit.

---

## 📦 Overview

This suite includes:
- 🧠 Research assistants (trend, competitor, action)
- 📊 Streamlit dashboard with 6 interactive tabs
- ✅ Export, audit logging, and Notion sync
- ☁️ Deployable on Streamlit Cloud
- 🧭 Modular design across 4 strategic build phases

---

## 🧱 Folder Structure

```bash
modular_research_suite/
├── Phase 1/  # Core runner + inputs + outputs
├── Phase 2/  # Full-stack loop executor
├── Phase 3/  # Notion sync + CSV logging
├── Phase 4/  # Assistants + UI tabs
├── main_app.py
├── requirements.txt
├── .env.template
└── outputs/YYYY-MM-DD/
```

---

## 🚀 Streamlit Tabs

| Tab              | Function                                 |
|------------------|------------------------------------------|
| Research Viewer  | View GPT summaries from research         |
| Trend Synthesizer| Display top emerging trends              |
| Competitor Watcher| Analyze competitor movements            |
| Action Generator | Recommend next strategic moves           |
| Assistant Tools  | Download files, add tags, log results    |
| Audit Log        | Filter + search session logs             |

---

## 📈 Phase 4 Summary

| Assistant            | Output File         | Dashboard Tab           |
|----------------------|----------------------|--------------------------|
| Trend Synthesizer    | `trend_report.md`    | Trend Synthesizer        |
| Competitor Watcher   | `competitor_report.md` | Competitor Watcher     |
| Action Generator     | `action_plan.md`     | Action Generator         |
| Research Viewer      | `summary.md`         | Research Viewer          |
| Audit Log            | `assistant_log.csv`  | Audit Log                |
| Export Tools         | File Downloads       | Assistant Tools          |

---

## 🏆 Certificate of Completion – Phase 4

**Version:** v1.0  
**Release Type:** Production-ready  
**Maintainer:** Mike Miller  
**Status:** ✅ All 4 Phases Complete

---

## ✅ GitHub + Streamlit Setup

1. Push repo to GitHub
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Set `main_app.py` as the entry point
4. Add secrets under `Settings → Secrets`:

```toml
OPENAI_API_KEY = "sk-..."
NOTION_API_KEY = "ntn-..."
NOTION_DATABASE_ID = "1cfbd31f04638060ba7ec9c779e20733"
```

---

## 🧠 Inspired Use Cases

- VC & AI trend analysis
- Founder intelligence tools
- Competitive landscape monitoring
- Action synthesis and business mapping

---

Developed as part of the Modular Assistant Build Series  
Licensed MIT • Follow for future versions (v1.1 → v2.0)

