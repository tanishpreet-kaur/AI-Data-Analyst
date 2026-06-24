import streamlit as st
from graph.workflow import analyst_bot
import tempfile
from langchain_community.utilities import SQLDatabase

# Page Config
st.set_page_config(
    page_title="AI Data Analyst",
    layout="wide"
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    st.title("AI Data Analyst")

    uploaded_db = st.file_uploader(
        "Upload Database",
        type=["db", "sqlite", "sqlite3"]
    )

    st.divider()

    st.subheader("Example Questions")
    st.markdown("""
    - What are the top selling products?
    - Show monthly revenue trend.
    - Which customers generated the most revenue?
    - What insights can you find?
    """)

# Main Header
st.title("AI Data Analyst")
st.caption("Ask questions about your data...")

# Dataset Preview
if uploaded_db:
    # Save uploaded file temporarily
    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".db"
    )

    temp_file.write(uploaded_db.read())
    temp_file.close()

    db_path = temp_file.name

    # Create SQLDatabase object
    db = SQLDatabase.from_uri(
        f"sqlite:///{db_path}"
    )

    st.success("Database loaded successfully!")

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if "table" in message:
            st.dataframe(message["table"])

# User Input
prompt = st.chat_input("Ask a question about your data...")

if prompt:
    # Add User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant Response
    with st.chat_message("assistant"):
        with st.spinner("Analyzing data..."):
            
            response = analyst_bot.invoke({
                "question": prompt
            })

            st.markdown(response["answer"])

            with st.expander("Insights"):
                st.markdown(response["key_findings"])

            assistant_message = {
                "role": "assistant",
                "content": response["answer"]
            }

            st.session_state.messages.append(
                assistant_message
            )