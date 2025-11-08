# explain_with_llm.py
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def explain_news_result(news_text, prediction):
    prompt = f"""
    The following news article was classified as {prediction}.
    Provide a short 3-line explanation why this classification might make sense.

    News:
    {news_text[:1000]}  # limit for safety
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
