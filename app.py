
import streamlit as st

from agent import run_agent
from memory.history import get_history


# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="AI Agent Automation System",
    page_icon="🤖",
    layout="wide"
)


# ==========================================
# 2. SESSION STATE
# ==========================================

if "latest_result" not in st.session_state:
    st.session_state.latest_result = None


# ==========================================
# 3. FUNCTION TO DISPLAY RESULTS
# ==========================================

def display_result(result):

    if isinstance(result, (dict, list)):

        st.json(result)

    else:

        st.write(result)


# ==========================================
# 4. SIDEBAR
# ==========================================

with st.sidebar:

    st.title("🤖 AI Agent")

    st.write("AI Agent & Automation System")

    st.divider()

    st.subheader("📌 Project Overview")

    st.write(
        "An intelligent assistant that understands user instructions, "
        "creates task plans, and executes tasks using available tools."
    )

    st.divider()

    st.subheader("🛠️ Available Tools")

    st.write("🧮 Calculator")
    st.caption("Performs mathematical calculations.")

    st.write("🕒 Date and Time")
    st.caption("Provides the current date and time.")

    st.write("🌤️ Weather")
    st.caption("Retrieves current weather information.")

    st.write("📁 File Operations")
    st.caption("Creates and reads text files.")

    st.divider()

    st.subheader("💡 Example Instructions")

    st.code("Calculate 2500 + 3500")
    st.code("Tell me today's date")
    st.code("Get weather in Hyderabad")
    st.code("Create a file named notes")

    st.divider()

    st.subheader("💻 Technologies")

    st.write("- Python")
    st.write("- Groq API")
    st.write("- Streamlit")
    st.write("- WeatherAPI")
    st.write("- JSON")

    st.divider()

    st.caption("AI Agent Automation System")


# ==========================================
# 5. APPLICATION TITLE
# ==========================================

st.title("🤖 AI Agent & Automation System")

st.write(
    "An intelligent assistant that understands instructions, "
    "creates task plans, and executes automated tasks."
)

st.divider()


# ==========================================
# 6. PROJECT DASHBOARD
# ==========================================

history = get_history()

st.header("📊 Project Dashboard")

total_conversations = len(history)

successful_conversations = 0
error_conversations = 0
total_tool_executions = 0

for item in history:

    result = item.get("result", {})

    status = result.get("status")

    if status == "completed":

        successful_conversations += 1

    elif status in ["completed_with_errors", "failed"]:

        error_conversations += 1

    total_tool_executions += len(result.get("results", []))


col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Conversations", total_conversations)

col2.metric("Successful Conversations", successful_conversations)

col3.metric("Conversations With Errors", error_conversations)

col4.metric("Tool Executions", total_tool_executions)


st.divider()


# ==========================================
# 7. TOOL USAGE ANALYTICS
# ==========================================

st.header("📈 Tool Usage Analytics")

tool_usage = {
    "Calculator": 0,
    "Date and Time": 0,
    "Weather": 0,
    "File Operations": 0
}

tool_mapping = {
    "calculator": "Calculator",
    "datetime": "Date and Time",
    "weather": "Weather",
    "file": "File Operations"
}


for item in history:

    result = item.get("result", {})

    for task in result.get("results", []):

        tool_name = task.get("tool")

        if tool_name in tool_mapping:

            display_name = tool_mapping[tool_name]

            tool_usage[display_name] += 1


tool_col1, tool_col2, tool_col3, tool_col4 = st.columns(4)

tool_col1.metric("🧮 Calculator", tool_usage["Calculator"])

tool_col2.metric("🕒 Date and Time", tool_usage["Date and Time"])

tool_col3.metric("🌤️ Weather", tool_usage["Weather"])

tool_col4.metric("📁 File Operations", tool_usage["File Operations"])


st.subheader("Tool Execution Chart")

st.bar_chart(tool_usage)


st.divider()


# ==========================================
# 8. AI AGENT INSTRUCTION SECTION
# ==========================================

st.header("💬 Ask Your AI Agent")

with st.form("agent_form"):

    user_instruction = st.text_area(
        "Enter your instruction:",
        placeholder="Example: Calculate 2500 + 3500",
        height=100
    )

    submit = st.form_submit_button(
        "Execute Task",
        use_container_width=True
    )


# ==========================================
# 9. EXECUTE USER INSTRUCTION
# ==========================================

if submit:

    if user_instruction.strip():

        with st.spinner(
            "AI Agent is planning and executing your task..."
        ):

            result = run_agent(user_instruction)

        st.session_state.latest_result = result

        st.rerun()

    else:

        st.warning("Please enter an instruction.")


# ==========================================
# 10. DISPLAY AGENT RESULTS
# ==========================================

if st.session_state.latest_result:

    result = st.session_state.latest_result

    st.subheader("📋 Agent Results")

    if result["status"] == "completed":

        st.success("Task completed successfully!")

    elif result["status"] == "completed_with_errors":

        st.warning("Task completed with some errors.")

    else:

        st.error("Task execution failed.")


    if result.get("results"):

        for index, item in enumerate(
            result["results"],
            start=1
        ):

            with st.container(border=True):

                st.subheader(f"Task {index}")

                st.write(
                    "**Task:**",
                    item.get("task", "Unknown task")
                )

                st.write(
                    "**Selected Tool:**",
                    item.get("tool", "Unknown tool")
                )

                st.write("**Result:**")

                # Correctly display numbers, text and JSON objects
                display_result(item.get("result"))


    elif result.get("error"):

        st.error(result["error"])


    with st.expander("View Complete Agent Response"):

        st.json(result)


st.divider()


# ==========================================
# 11. CONVERSATION HISTORY
# ==========================================

st.header("📚 Conversation History")

history = get_history()

if history:

    st.write(f"Total conversations: {len(history)}")

    for index, item in enumerate(
        reversed(history),
        start=1
    ):

        instruction = item.get(
            "instruction",
            "Unknown instruction"
        )

        with st.expander(
            f"Conversation {index}: {instruction}"
        ):

            st.write(
                "**Time:**",
                item.get("timestamp", "Unknown")
            )

            st.write(
                "**Instruction:**",
                instruction
            )

            st.write("**Result:**")

            display_result(item.get("result", {}))


else:

    st.info("No previous conversations found.")


# ==========================================
# 12. FOOTER
# ==========================================

st.divider()

st.caption(
    "AI Agent & Automation System | Python | Groq | Streamlit"
)
