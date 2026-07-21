import streamlit as st
import requests



BASE_URL = "https://enterprise-prompt-engineering-toolkit.onrender.com"
# ==============================
# Page Configuration
# ==============================
st.set_page_config(
    page_title="Enterprise Prompt Engineering Toolkit",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#0f172a,#1e293b,#111827);
    color:white;
}

section[data-testid="stSidebar"]{
    background:#111827;
}

h1,h2,h3{
    color:white;
}

div[data-testid="metric-container"]{
    background:#1f2937;
    border-radius:15px;
    padding:20px;
    box-shadow:0 0 15px rgba(0,0,0,.3);
}

.stButton>button{
    background:#2563eb;
    color:white;
    border-radius:10px;
    border:none;
}

.stButton>button:hover{
    background:#1d4ed8;
}

textarea,input{
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# ==============================
# Sidebar
# ==============================
st.sidebar.title("🤖 Enterprise Prompt Toolkit")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "📝 Prompt Builder",
        "📚 Prompt Library",
        "⭐ Prompt Evaluator",
        "🚀 Prompt Optimizer",
        "🤖 Model Comparison",
        "🕒 Version History",
        "📊 Analytics"
    ]
)

st.markdown("""

### AI Powered Prompt Builder • Evaluator • Optimizer • Model Comparison
""")


# ==============================
# Dashboard
# ==============================
if page == "🏠 Dashboard":

    st.title("🤖 Enterprise Prompt Engineering Toolkit")

    try:

        response = requests.get(f"{BASE_URL}/analytics")

        if response.status_code == 200:

            data = response.json()

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "📄 Total Prompts",
                    data["total_prompts"]
                )

            with col2:
                st.metric(
                    "🕒 Prompt Versions",
                    data["total_versions"]
                )

            with col3:
                st.metric(
                    "🤖 Models",
                    len(data["available_models"])
                )

            st.divider()

            st.subheader("Latest Prompt")

            st.success(data["latest_prompt"])

            st.subheader("Average Versions")

            st.info(data["average_versions"])

            st.subheader("Available Models")

            for model in data["available_models"]:
                st.write("✅", model)

        else:
            st.error("Failed to connect to FastAPI")

    except Exception as e:

        st.error(f"Backend Error: {e}")
    
if page == "📝 Prompt Builder":

    st.title("📝 Prompt Builder")

    title = st.text_input("Title")
    role = st.text_area("Role")
    context = st.text_area("Context")
    task = st.text_area("Task")
    rules = st.text_area("Rules")
    output_format = st.text_input("Output Format")

    if st.button("🚀 Generate Prompt"):

        if not title or not role or not context or not task:

            st.warning("⚠️ Please fill all required fields.")

        else:

            payload = {
                "title": title,
                "role": role,
                "context": context,
                "task": task,
                "rules": rules,
                "output_format": output_format
            }

            with st.spinner("Generating Prompt..."):

                response = requests.post(
                    f"{BASE_URL}/build_prompt",
                    json=payload
                )

            if response.status_code == 200:

                data = response.json()

                st.success("✅ Prompt Generated Successfully")

                st.subheader("Generated Prompt")

                st.code(
                    data["prompt"],
                    language="text"
                )

                st.download_button(
                    label="📥 Download Prompt",
                    data=data["prompt"],
                    file_name="generated_prompt.txt",
                    mime="text/plain"
                )

            else:

                st.error("❌ Failed to generate prompt")

if page == "📚 Prompt Library":

    st.title("📚 Prompt Library")

    response = requests.get(f"{BASE_URL}/prompts")

    if response.status_code == 200:

        prompts = response.json()

        if len(prompts) == 0:

            st.info("No prompts available.")

        else:

            for prompt in prompts:

                with st.expander(prompt["title"]):

                    st.write("### Role")
                    st.write(prompt["role"])

                    st.write("### Context")
                    st.write(prompt["context"])

                    st.write("### Task")
                    st.write(prompt["task"])

                    st.write("### Rules")
                    st.write(prompt["rules"])

                    st.write("### Output Format")
                    st.write(prompt["output_format"])

                    st.code(prompt["content"])

                    # 👇 ADD HERE
                    if st.button(
                        "🗑 Delete",
                        key=f"delete_{prompt['id']}"
                    ):

                        requests.delete(
                            f"{BASE_URL}/prompts/{prompt['id']}"
                        )

                        st.success("Prompt Deleted")

                        st.rerun()

if page == "⭐ Prompt Evaluator":

    st.title("⭐ Prompt Evaluator")

    prompt = st.text_area(
        "Enter Prompt",
        height=300
    )

    if st.button(
        "Evaluate Prompt",
        key="evaluate"
    ):

        if prompt == "":

            st.warning("Please enter a prompt.")

        else:

            payload = {
                "prompt": prompt
            }

            with st.spinner("Evaluating..."):

                response = requests.post(
                    f"{BASE_URL}/evaluate",
                    json=payload
                )

            if response.status_code == 200:

                result = response.json()

                st.success("Evaluation Completed")

                st.json(result)

            else:

                st.error("Evaluation Failed")

if page == "🚀 Prompt Optimizer":

    st.title("🚀 Prompt Optimizer")

    prompt = st.text_area(
        "Enter Prompt",
        height=300,
        key="optimizer_prompt"
    )

    if st.button(
        "Optimize Prompt",
        key="optimize"
    ):

        if prompt == "":

            st.warning("Please enter a prompt.")

        else:

            payload = {
                "prompt": prompt
            }

            with st.spinner("Optimizing Prompt..."):

                response = requests.post(
                    f"{BASE_URL}/optimize",
                    json=payload
                )

            if response.status_code == 200:

                result = response.json()

                st.success("Prompt Optimized Successfully")

                st.json(result)

            else:

                st.error("Optimization Failed")

if page == "🤖 Model Comparison":

    st.title("🤖 AI Model Comparison")

    prompt = st.text_area(
        "Enter Prompt",
        height=250,
        key="compare_prompt"
    )

    if st.button(
        "Compare Models",
        key="compare"
    ):

        if prompt == "":

            st.warning("Please enter a prompt.")

        else:

            payload = {
                "prompt": prompt
            }

            with st.spinner("Comparing Models..."):

                response = requests.post(
                    f"{BASE_URL}/compare_models",
                    json=payload
                )

            if response.status_code == 200:

                result = response.json()

                st.success("Comparison Completed")

                for model in result["comparison"]:

                    st.markdown("---")

                    st.subheader(f"🤖 {model['model']}")

                    if model["status"] == "success":

                        st.write(f"⏱ Response Time: {model['response_time']} sec")

                        st.write(f"📝 Word Count: {model['word_count']}")

                        st.text_area(
                            "Response",
                            value=model["response"],
                            height=300,
                            key=model["model"]
                        )

                    else:

                        st.error(model["error"])

            else:

                st.error("Comparison Failed")

if page == "🕒 Version History":

    st.title("🕒 Prompt Version History")

    prompt_id = st.number_input(
        "Enter Prompt ID",
        min_value=1,
        step=1
    )

    if st.button("Load Versions"):

        response = requests.get(
            f"{BASE_URL}/prompts/{prompt_id}/versions"
        )

        

        if response.status_code == 200:

            data = response.json()

            if "versions" not in data:

                st.warning(data.get("message", "No versions found"))

            else:

                versions = data["versions"]

                for version in versions:

                    with st.expander(f"Version {version['version']}"):

                        st.write("### Title")
                        st.write(version["title"])

                        st.write("### Role")
                        st.write(version["role"])

                        st.write("### Context")
                        st.write(version["context"])

                        st.write("### Task")
                        st.write(version["task"])

                        st.write("### Rules")
                        st.write(version["rules"])

                        st.write("### Output Format")
                        st.write(version["output_format"])

                        st.code(version["content"])

                        if st.button(
                            "Restore Version",
                            key=f"restore_{version['id']}"
                        ):

                            restore = requests.post(
                                f"{BASE_URL}/prompts/{prompt_id}/restore/{version['version']}"
                            )

                            if restore.status_code == 200:
                                st.success("Version Restored")
                                st.rerun()
                            else:
                                st.error("Restore Failed")

        else:

            st.error("Unable to load versions.")

if page == "📊 Analytics":

    st.title("📊 Analytics Dashboard")

    response = requests.get(f"{BASE_URL}/analytics")

    if response.status_code == 200:

        data = response.json()

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "📄 Total Prompts",
                data["total_prompts"]
            )

        with col2:
            st.metric(
                "🕒 Total Versions",
                data["total_versions"]
            )

        with col3:
            st.metric(
                "🤖 Models",
                len(data["available_models"])
            )

        st.divider()

        st.subheader("Latest Prompt")

        st.success(data["latest_prompt"])

        st.subheader("Average Versions")

        st.info(data["average_versions"])

        st.subheader("Available Models")

        for model in data["available_models"]:
            st.write("✅", model)

    else:

        st.error("Unable to load analytics.")