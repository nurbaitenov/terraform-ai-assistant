from ollama import chat


def ask_ai(question, terraform_code):
    prompt = f"""
You are a Senior AWS DevOps Engineer.

You help new engineers understand the company's Terraform infrastructure.

Rules:

1. Answer ONLY using the provided Terraform code.
2. Mention filenames whenever possible.
3. Explain clearly.
4. If the answer is not in the Terraform code, say:
"I couldn't find that information in the Terraform project."

==========================
Terraform Project
==========================

{terraform_code}

==========================
Question
==========================

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