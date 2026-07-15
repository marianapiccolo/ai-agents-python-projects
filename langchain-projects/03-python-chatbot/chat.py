import streamlit as st
from langchain_core.messages import HumanMessage

from openai_model import chain


def open_chat(prompt: str | None) -> None:
    """
    Display the user message and generate an AI response using the LangChain chain.
    """

    if prompt:
        # Create a simple conversation history with the user message
        messages = [
            HumanMessage(content=prompt)
        ]

        # Display the user message in the Streamlit chat interface
        for message in messages:
            if message.type != "system":
                with st.chat_message(message.type):
                    st.write(message.content)

        # Send the conversation history to the chain
        response = chain.invoke(
            {
                "history": messages
            }
        )

        # Display the AI response
        with st.chat_message("ai"):
            st.write(response.content)


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