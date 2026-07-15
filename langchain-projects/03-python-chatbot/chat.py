import streamlit as st

from openai_model import chain_with_memory


def open_chat(prompt: str | None) -> None:
    """
    Run the chatbot using LangChain message history and Streamlit interface.
    """

    # Initialize a visual message history for the Streamlit interface
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    messages = st.session_state["messages"]

    # If the user sends a new message, call the chain with memory
    if prompt:
        messages.append(
            {
                "role": "human",
                "content": prompt
            }
        )

        # Invoke the chain with a fixed session ID
        # The session ID tells LangChain which conversation history to use
        ai_response = chain_with_memory.invoke(
            {
                "message": prompt
            },
            config={
                "configurable": {
                    "session_id": "python-chat-session"
                }
            }
        )

        messages.append(
            {
                "role": "ai",
                "content": ai_response.content
            }
        )

    # Display the conversation history in Streamlit
    for message in messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])


def run_app() -> None:
    """
    Run the Streamlit chatbot application.
    """

    st.header("Python Learning Chatbot", divider=True)

    st.markdown("#### Ask questions about Python programming")

    prompt = st.chat_input("Type your prompt here")

    open_chat(prompt)


if __name__ == "__main__":
    run_app()