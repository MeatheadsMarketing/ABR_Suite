import streamlit as st
import os

st.subheader("📄 Research Summary Viewer")

base_dir = "outputs"
if not os.path.exists(base_dir):
    st.warning("No 'outputs' folder found.")
else:
    dates = sorted(os.listdir(base_dir), reverse=True)
    selected_date = st.selectbox("Select a date:", dates)

    file_path = os.path.join(base_dir, selected_date, "summary.md")

    st.subheader(f"🧠 GPT Summary – {selected_date}")
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            st.markdown(f.read())
    else:
        st.error("summary.md not found for selected date. Run the research loop first.")
