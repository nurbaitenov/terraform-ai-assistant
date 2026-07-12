import sys
import time

from ai import ask_ai
from config import DEBUG
from reader import get_latest_modified, load_terraform

terraform_cache = {}


def load_cache():
    if DEBUG:
        print("Loading Terraform into RAM...")

    start = time.time()

    terraform_code = load_terraform()

    terraform_cache["code"] = terraform_code
    terraform_cache["last_modified"] = get_latest_modified()
    terraform_cache["loaded_at"] = time.time()
    terraform_cache["size_bytes"] = sys.getsizeof(terraform_code)
    terraform_cache["characters"] = len(terraform_code)

    end = time.time()

    if DEBUG:
        print(f"Loaded in {end - start:.3f} seconds")
        print(f"Cache size: {terraform_cache['size_bytes'] / 1024:.2f} KB")
        print(f"Characters: {terraform_cache['characters']}")
        print()


def refresh_cache():
    current = get_latest_modified()

    if current != terraform_cache["last_modified"]:
        print("\nTerraform files changed.")
        print("Refreshing cache...\n")
        load_cache()


load_cache()


def ask(question):
    refresh_cache()
    return ask_ai(question, terraform_cache["code"])