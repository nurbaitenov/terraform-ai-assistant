from assistant import ask

print("=" * 60)
print("Terraform AI Assistant")
print("=" * 60)

while True:
    question = input("\nAsk (type 'exit' to quit): ")

    if question.lower() == "exit":
        break

    print("\nThinking...\n")

    answer = ask(question)

    print(answer)