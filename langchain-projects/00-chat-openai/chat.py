import streamlit as st
from langchain_core.messages import HumanMessage

from openai_model import messages, model


def open_chat(prompt, model, messages):
    """
    Run the chat interaction using Streamlit session state.

    The session state keeps the conversation history while the app is open.
    """

    # Check if there is already a conversation stored in the Streamlit session
    if "messages" in st.session_state:
        messages = st.session_state["messages"]
    else:
        st.session_state["messages"] = messages

    # If the user sends a message, add it to the conversation
    if prompt:
        messages.append(HumanMessage(content=prompt))

        # Send the conversation history to the model
        response = model.invoke(messages)

        # Add the model response to the conversation history
        messages.append(response)

    # Display all messages except the system message
    for message in messages:
        if message.type != "system":
            with st.chat_message(message.type):
                st.write(message.content)


def run_app():
    """
    Run the Streamlit chat application.
    """

    st.header("LangChain Chatbot", divider=True)

    st.markdown(
        "#### Chat with an OpenAI model using LangChain and Streamlit"
    )

    # Chat input field displayed at the bottom of the page
    prompt = st.chat_input("Type your message")

    # Start the chat interaction
    open_chat(prompt, model, messages)


if __name__ == "__main__":
    run_app()