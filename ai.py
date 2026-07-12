from ollama import chat

from config import MODEL
from prompts import SYSTEM_PROMPT


def ask_ai(question, terraform_code):
    try:
        response = chat(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": f"""
Terraform Project:

{terraform_code}

Question:

{question}
""",
                },
            ],
        )

        return response["message"]["content"]

    except Exception as e:
        return f"AI Error: {e}"