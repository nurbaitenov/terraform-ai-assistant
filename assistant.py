import time
import sys

from reader import load_terraform
from ai import ask_ai

print("Loading Terraform cache...")

start = time.time()

terraform_code = load_terraform()

terraform_cache = {
    "code": terraform_code,
    "loaded_at": time.time(),
    "size_bytes": sys.getsizeof(terraform_code),
    "size_kb": sys.getsizeof(terraform_code) / 1024,
    "characters": len(terraform_code),
}

end = time.time()

print(f"Terraform loaded in {end - start:.3f} seconds.")
print(f"Cache size: {terraform_cache['size_kb']:.2f} KB")
print(f"Characters: {terraform_cache['characters']}")
print(f"Memory address: {id(terraform_cache['code'])}")


def ask(question):
    return ask_ai(question, terraform_cache["code"])