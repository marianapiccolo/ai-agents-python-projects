import streamlit as st


def generate_text() -> None:
    """Display the text generation tool."""
    st.write("Text generation tool selected.")


def summarize_text() -> None:
    """Display the text summarization tool."""
    st.write("Text summarization tool selected.")


def open_chat() -> None:
    """Display the chat tool."""
    st.write("Chat tool selected.")


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

    # Display the selected tool
    if selected_tool == options[0]:
        generate_text()
    elif selected_tool == options[1]:
        summarize_text()
    else:
        open_chat()


if __name__ == "__main__":
    main_app()