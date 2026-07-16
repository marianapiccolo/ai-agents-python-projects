import streamlit as st

from hfapi_summarization import summarize_text


def generate_text(prompt: str | None) -> None:
    """Display the text generation tool."""

    st.write("Text generation tool selected.")

    if prompt:
        st.write("Generated text will appear here.")


def summarize(prompt: str | None) -> None:
    """Summarize the text provided by the user."""

    st.markdown("##### Paste the text you want to summarize in the prompt box.")

    if prompt:
        summary = summarize_text(prompt)
        st.write(summary)


def open_chat(prompt: str | None) -> None:
    """Display the chat tool."""

    st.write("Chat tool selected.")

    if prompt:
        st.write("Chat response will appear here.")


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
        generate_text(prompt)
    elif selected_tool == options[1]:
        summarize(prompt)
    else:
        open_chat(prompt)


if __name__ == "__main__":
    main_app()