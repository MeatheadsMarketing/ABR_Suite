import streamlit as st
import os
from datetime import datetime
import importlib.util

st.set_page_config(page_title="Modular Research Suite", layout="wide")

tabs = [
    "Research Viewer",
    "Trend Synthesizer",
    "Competitor Watcher",
    "Action Generator",
    "Assistant Tools",
    "Audit Log"
]
selected_tab = st.sidebar.radio("🔎 Select Tab", tabs)

st.title("📊 Modular Research Suite")

def load_module(script_path, module_name):
    if os.path.exists(script_path):
        spec = importlib.util.spec_from_file_location(module_name, script_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    else:
        st.warning(f"Missing file: {script_path}")

if selected_tab == "Research Viewer":
    load_module("streamlit_output_viewer.py", "streamlit_output_viewer")

elif selected_tab == "Trend Synthesizer":
    load_module("trend_tab.py", "trend_tab")

elif selected_tab == "Competitor Watcher":
    load_module("competitor_tab.py", "competitor_tab")

elif selected_tab == "Action Generator":
    load_module("action_tab.py", "action_tab")

elif selected_tab == "Assistant Tools":
    load_module("dashboard_tools.py", "dashboard_tools")

elif selected_tab == "Audit Log":
    load_module("audit_log_tab.py", "audit_log_tab")
