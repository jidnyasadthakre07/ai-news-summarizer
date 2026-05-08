import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "models/gemini-flash-latest"
)


def generate_summary(article, language):

    prompt = f"""
    Summarize this article in 3 concise bullet points.

    Output language: {language}

    Article:
    {article}
    """

    response = model.generate_content(prompt)

    return response.text


def generate_headlines(article, tone, language):

    prompt = f"""
    Generate 5 professional news headlines.

    Tone: {tone}

    Output language: {language}

    Rules:
    - Under 10 words
    - No clickbait

    Article:
    {article}
    """

    response = model.generate_content(prompt)

    return response.text


def detect_category(article):

    prompt = f"""
    Classify this article into one category:

    - Technology
    - Sports
    - Politics
    - Business
    - Entertainment
    - Health

    Return only category name.

    Article:
    {article}
    """

    response = model.generate_content(prompt)

    return response.text.strip()