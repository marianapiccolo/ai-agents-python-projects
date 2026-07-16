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

    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {
                "role": "system",
                "content": "Answer the questions correctly and accurately."
            }
        ]

    messages = st.session_state["messages"]

    if prompt:
        user_message = {
            "role": "user",
            "content": prompt
        }

        messages.append(user_message)

        updated_messages = complete_chat(messages)

        st.session_state["messages"] = updated_messages

    for message in st.session_state["messages"]:
        role = message["role"]
        content = message["content"]

        if role == "system":
            continue

        with st.chat_message(role):
            st.write(content)


def main_app() -> None:
    """Run the main Streamlit application."""

    st.header("AI Assistant Tools", divider=True)

    st.markdown(
        "#### Choose an AI tool, write your prompt, and get an intelligent response."
    )

    options = [
        "Generate Text",
        "Summarize Text",
        "Open Chat"
    ]

    selected_tool = st.selectbox(
        "Select the AI tool you want to use",
        options=options
    )

    prompt = st.chat_input("Type your prompt here")

    if selected_tool == options[0]:
        text_generator(prompt)
    elif selected_tool == options[1]:
        text_summarizer(prompt)
    else:
        open_chat(prompt)


if __name__ == "__main__":
    main_app()