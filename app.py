import streamlit as st

from utils import (
    generate_summary,
    generate_headlines,
    detect_category
)

st.set_page_config(
    page_title="AI News Generator",
    page_icon="📰",
    layout="centered"
)

st.title("📰 AI News Summarizer & Headline Generator")

st.markdown(
    "Generate summaries and headlines using Gemini AI."
)

article = st.text_area(
    "Paste News Article",
    height=300,
    placeholder="Paste article here..."
)

language = st.selectbox(
    "Select Output Language",
    [
        "English",
        "Hindi",
        "French",
        "Spanish",
        "German"
    ]
)

tone = st.selectbox(
    "Select Headline Tone",
    [
        "Formal",
        "Catchy",
        "SEO-Friendly",
        "Breaking News"
    ]
)

if st.button("Generate"):

    if not article.strip():

        st.warning("Please paste an article.")

    else:

        try:

            with st.spinner("Generating AI content..."):

                category = detect_category(article)

                summary = generate_summary(
                    article,
                    language
                )

                headlines = generate_headlines(
                    article,
                    tone,
                    language
                )

                st.success("Content Generated Successfully")

                st.subheader("🗂 News Category")
                st.info(category)

                st.subheader("📌 Summary")
                st.markdown(summary)

                st.subheader("📰 Headlines")

                for h in headlines.split("\n"):

                    if h.strip():

                        st.markdown(f"- {h}")

        except Exception as e:

            st.error(str(e))