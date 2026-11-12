
from groq import Groq

from config.settings import GROQ_API_KEY, GROQ_MODEL
from reviewer.prompts import (
    SYSTEM_PROMPT,
    create_review_prompt
)


# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)


def generate_review(code, analysis_results):
    """
    Generate an AI-powered Python code review.
    """

    user_prompt = create_review_prompt(
        code,
        analysis_results
    )

    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        temperature=0.2,
        max_completion_tokens=4000
    )

    review = response.choices[0].message.content

    usage = response.usage

    token_details = {
        "prompt_tokens": usage.prompt_tokens,
        "completion_tokens": usage.completion_tokens,
        "total_tokens": usage.total_tokens
    }

    return {
        "review": review,
        "tokens": token_details,
        "model": GROQ_MODEL
    }
