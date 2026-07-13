import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage

from huggingface_model import messages, model


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

        response_content = response.content

        # Some reasoning models return internal thinking before </think>.
        # This keeps only the final answer after the thinking section.
        if "</think>" in response_content:
            final_answer = response_content.split("</think>", 1)[1].strip()
            messages.append(AIMessage(content=final_answer))
        else:
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
        "#### Chat with a Hugging Face model using LangChain and Streamlit"
    )

    # Chat input field displayed at the bottom of the page
    prompt = st.chat_input("Type your message")

    # Start the chat interaction
    open_chat(prompt, model, messages)


if __name__ == "__main__":
    run_app()