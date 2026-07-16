import streamlit as st

from hfapi_chat_completion import complete_chat
from hfapi_summarization import summarize_text
from hfapi_text_generation import generate_text


def text_generator(prompt: str | None) -> None:
    """Generate text from the user prompt."""

    st.markdown("##### Ask the system to generate a text for you.")

    if prompt:
        generated_text = generate_text(prompt)
        st.write(generated_text)


def text_summarizer(prompt: str | None) -> None:
    """Summarize the text provided by the user."""

    st.markdown("##### Paste the text you want to summarize in the prompt box.")

    if prompt:
        summarized_text = summarize_text(prompt)
        st.write(summarized_text)


def open_chat(prompt: str | None) -> None:
    """Open a chat interface with the AI model."""

    st.markdown("##### Chat with the AI assistant.")

    # Store the conversation history in Streamlit session state
    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {
                "role": "system",
                "content": "Answer the questions correctly and accurately."
            }
        ]

    messages = st.session_state["messages"]

    # Add the user message and call the model
    if prompt:
        user_message = {
            "role": "user",
            "content": prompt
        }

        messages.append(user_message)

        updated_messages = complete_chat(messages)

        st.session_state["messages"] = updated_messages

    # Display the conversation, ignoring the system message
    for message in st.session_state["messages"]:
        if message["role"] == "system":
            continue

        role = "user" if message["role"] == "user" else "assistant"

        with st.chat_message(role):
            st.write(message["content"])


def main_app() -> None:
    """Run the main Streamlit application."""

    # Main title
    st.header("AI Assistant Tools", divider=True)

    # Subtitle
    st.markdown(
        "#### Choose an AI tool, write your prompt, and get an intelligent response."
    )

    # Available AI tools
    options = [
        "Generate Text",
        "Summarize Text",
        "Open Chat"
    ]

    # Tool selection
    selected_tool = st.selectbox(
        "Select the AI tool you want to use",
        options=options
    )

    # Prompt input field
    prompt = st.chat_input("Type your prompt here")

    # Run the selected tool
    if selected_tool == options[0]:
        text_generator(prompt)
    elif selected_tool == options[1]:
        text_summarizer(prompt)
    else:
        open_chat(prompt)


if __name__ == "__main__":
    main_app()