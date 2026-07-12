from reader import load_terraform
from ai import ask_ai


def ask(question):
    terraform_code = load_terraform()

    answer = ask_ai(question, terraform_code)

    return answer