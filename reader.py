import os

from config import TERRAFORM_PATH


def load_terraform(terraform_path=TERRAFORM_PATH):
    terraform_code = ""

    for root, dirs, files in os.walk(terraform_path):
        for file in files:
            if (
                file.endswith(".tf")
                or file.endswith(".tfvars")
                or file.endswith(".tfvars.json")
            ):
                path = os.path.join(root, file)

                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()

                terraform_code += f"\n===== FILE: {path} =====\n"
                terraform_code += content
                terraform_code += "\n"

    return terraform_code


def get_latest_modified(terraform_path=TERRAFORM_PATH):
    latest = 0

    for root, dirs, files in os.walk(terraform_path):
        for file in files:
            if (
                file.endswith(".tf")
                or file.endswith(".tfvars")
                or file.endswith(".tfvars.json")
            ):
                path = os.path.join(root, file)

                modified = os.path.getmtime(path)

                if modified > latest:
                    latest = modified

    return latest