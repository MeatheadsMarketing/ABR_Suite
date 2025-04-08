import streamlit as st
import os
import csv

st.subheader("📦 Assistant Tools & Export + Status Center")

base_dir = "outputs"
log_file = "assistant_log.csv"

if not os.path.exists(base_dir):
    st.warning("No output folders found.")
else:
    dates = sorted(os.listdir(base_dir), reverse=True)
    selected_date = st.selectbox("Select a date to audit/export:", dates)
    folder_path = os.path.join(base_dir, selected_date)

    st.markdown(f"### 📋 File Status for `{selected_date}`:")
    files_to_check = [
        "summary.md",
        "trend_report.md",
        "competitor_report.md",
        "action_plan.md"
    ]

    file_status = {}
    for file in files_to_check:
        exists = os.path.exists(os.path.join(folder_path, file))
        file_status[file] = "✅ Found" if exists else "❌ Missing"
        st.markdown(f"- **{file}**: {file_status[file]}")

    st.markdown("### 🏷️ Tag This Session:")
    tags = st.text_input("Enter comma-separated tags (e.g., AI, Trends, Risk):")
    notes = st.text_area("Add any notes (optional):")

    if st.button("📤 Export to CSV Log"):
        log_entry = {
            "Date": selected_date,
            "summary.md": file_status["summary.md"],
            "trend_report.md": file_status["trend_report.md"],
            "competitor_report.md": file_status["competitor_report.md"],
            "action_plan.md": file_status["action_plan.md"],
            "Tags": tags,
            "Notes": notes
        }

        file_exists = os.path.exists(log_file)
        with open(log_file, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=log_entry.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(log_entry)
        st.success("✅ Entry exported to assistant_log.csv")
