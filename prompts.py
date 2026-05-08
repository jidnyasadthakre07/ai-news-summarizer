SUMMARY_PROMPT = """
You are a professional news editor.

Summarize the following article in exactly 3 concise bullet points.

Rules:
- Each bullet under 20 words
- Keep factual accuracy
- No opinions
- Clear language

Article:
{article}
"""

HEADLINE_PROMPT = """
You are a senior newsroom headline editor.

Generate 5 headlines.

Tone: {tone}

Rules:
- Factual
- Engaging but not clickbait
- Under 12 words
- Avoid exaggeration
- Do not invent facts

Article:
{article}
"""