import streamlit as st
from langchain_core.messages import HumanMessage

from openai_model import chain


def open_chat(prompt: str | None, chain) -> None:
    """
    Run the chatbot using Streamlit session state to store message history.
    """

    # Initialize the message history in Streamlit session state
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    messages = st.session_state["messages"]

    # If the user sends a new message, add it to the history and call the chain
    if prompt:
        messages.append(HumanMessage(content=prompt))

        # Send the full conversation history to the chain
        ai_response = chain.invoke(
            {
                "history": messages
            }
        )

        # Add the AI response to the message history
        messages.append(ai_response)

    # Display all messages stored in the conversation history
    for message in messages:
        if message.type != "system":
            with st.chat_message(message.type):
                st.write(message.content)


def run_app() -> None:
    """
    Run the Streamlit chatbot application.
    """

    st.header("Python Learning Chatbot", divider=True)

    st.markdown("#### Ask questions about Python programming")

    prompt = st.chat_input("Type your prompt here")

    open_chat(prompt, chain)


if __name__ == "__main__":
    run_app()