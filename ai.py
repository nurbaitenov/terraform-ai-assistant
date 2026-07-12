from ollama import chat


def ask_ai(question, terraform_code):
    prompt = f"""
You are a Senior AWS DevOps Engineer.

Your task is to help new engineers understand the company's Terraform infrastructure.

Rules:
- Answer ONLY using the provided Terraform code.
- Mention filenames whenever possible.
- If you cannot find the answer, say:
"I couldn't find that information in the Terraform project."

========================
Terraform Project
========================

{terraform_code}

========================
Question
========================

{question}
"""

    response = chat(
        model="deepseek-r1:1.5b",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response["message"]["content"]