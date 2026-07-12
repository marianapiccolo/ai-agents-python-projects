import streamlit as st

from caption_generator import generate_captions


def run_app() -> None:
    """
    Run the Streamlit interface for the video caption generator.
    """

    st.header("Video Caption Generator", divider=True)

    st.markdown(
        "Generate subtitles automatically from a video or audio file using OpenAI speech-to-text."
    )

    context_prompt = st.text_input(
        "Add some context about the content to improve the transcription:",
        placeholder="Example: This is Portuguese content about software development."
    )

    uploaded_file = st.file_uploader(
        "Upload a video or audio file",
        type=["mp4", "mp3", "wav", "m4a"]
    )

    if uploaded_file:
        with st.spinner("Generating captions..."):
            captions = generate_captions(uploaded_file, context_prompt)

        st.success(f"File '{uploaded_file.name}' was captioned successfully.")

        st.markdown("### Generated captions")
        st.text_area(
            label="SRT output",
            value=captions,
            height=300
        )

        st.download_button(
            label="Download SRT file",
            data=captions,
            file_name="captions.srt",
            mime="text/plain"
        )


if __name__ == "__main__":
    run_app()