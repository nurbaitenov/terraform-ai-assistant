import os


def load_terraform(terraform_path="terraform"):
    print("Loading Terraform files into RAM...")

    terraform_code = ""

    for root, dirs, files in os.walk(terraform_path):
        for file in files:
            if (
                file.endswith(".tf")
                or file.endswith(".tfvars")
                or file.endswith(".tfvars.json")
            ):
                path = os.path.join(root, file)

                print(f"Reading: {path}")

                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()

                terraform_code += f"\n===== FILE: {path} =====\n"
                terraform_code += content
                terraform_code += "\n"

    return terraform_code