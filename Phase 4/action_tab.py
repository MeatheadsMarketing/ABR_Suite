import streamlit as st
import os

st.subheader("🎯 Action Plan Viewer")

base_dir = "outputs"
if not os.path.exists(base_dir):
    st.warning("No 'outputs' folder found. Please run a research session first.")
else:
    dates = sorted(os.listdir(base_dir), reverse=True)
    selected_date = st.selectbox("Select a date:", dates)

    report_path = os.path.join(base_dir, selected_date, "action_plan.md")

    st.subheader(f"📌 Strategic Actions – {selected_date}")
    if os.path.exists(report_path):
        with open(report_path, "r") as f:
            st.markdown(f.read())
    else:
        st.error("action_plan.md not found. Run action_generator.py first.")
