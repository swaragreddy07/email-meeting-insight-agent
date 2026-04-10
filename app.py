import streamlit as st
import tempfile
import os
import json
import re
from agent.workflow import create_workflow
from agent.utils import load_text_files

# ---------- Page Setup ----------
st.set_page_config(page_title="Email & Meeting Insight Agent", layout="centered")
st.title("📧 Email & Meeting Insight Agent")
st.write("Upload one or more `.txt` files to extract action items and summaries.")

# ---------- File Upload ----------
uploaded_files = st.file_uploader("Upload files", type=["txt"], accept_multiple_files=True)

if uploaded_files:
    temp_dir = tempfile.mkdtemp()
    for file in uploaded_files:
        with open(os.path.join(temp_dir, file.name), "wb") as f:
            f.write(file.getbuffer())

    st.info("Processing your files... please wait ⏳")

    # ---------- Run the Agent ----------
    emails = load_text_files(temp_dir)
    app = create_workflow()
    result = app.invoke({"emails": emails, "entities": {}, "summary": "", "memory": []})

    # ---------- Summary Section ----------
    st.subheader("📄 Summary")
    st.write(result.get("summary", "No summary generated."))

    st.subheader("🧠 Extracted Entities & Tasks")

    raw_entities = result.get("entities", "")

    try:
        cleaned = re.sub(r"```(json)?", "", raw_entities).replace("```", "").strip()
        entities_json = json.loads(cleaned)
        st.json(entities_json)
    except Exception as e:
        st.error(f"Json Parse Error: {e}")
        st.text_area("Raw Output", raw_entities, height=200)

    # ---------- Memory Section ----------
    st.subheader("💭 Memory Context (optional)")
    st.write(result.get("memory", []))
