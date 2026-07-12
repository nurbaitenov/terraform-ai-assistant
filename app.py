from assistant import ask
from config import APP_NAME, EXIT_COMMAND

print("=" * 60)
print(APP_NAME)
print("=" * 60)

while True:
    question = input(f"\nAsk (type '{EXIT_COMMAND}' to quit): ")

    if question.lower() == EXIT_COMMAND:
        print("Goodbye!")
        break

    print("\nThinking...\n")

    answer = ask(question)

    print(answer)