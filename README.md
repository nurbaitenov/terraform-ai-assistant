# Terraform AI Assistant

## Overview

Terraform AI Assistant is a local AI-powered tool that helps DevOps engineers understand Terraform infrastructure. It reads Terraform files, caches them in RAM, and uses DeepSeek running on Ollama to answer infrastructure-related questions.

---

## Features

- Reads `.tf`, `.tfvars`, and `.tfvars.json` files
- Automatic RAM cache with refresh
- Local AI using Ollama + DeepSeek
- Interactive command-line interface

---

## Project Structure

```text
terraform-ai-assistant/
│
├── app.py          # CLI
├── assistant.py    # Application logic
├── ai.py           # AI communication
├── reader.py       # Terraform reader
├── config.py       # Configuration
├── prompts.py      # AI prompt
├── terraform/      # Terraform project
└── README.md
```

---

## Workflow

```text
User
  │
  ▼
app.py
  │
  ▼
assistant.py
  ├── reader.py
  └── ai.py
          │
          ▼
  Ollama + DeepSeek
          │
          ▼
       Response
```

---

## Installation

```bash
git clone <repository-url>
cd terraform-ai-assistant

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

ollama pull deepseek-r1:1.5b

python app.py
```

---

## Example

```text
Ask:
> Which module creates the RDS?

Answer:
The RDS resources are defined in modules/rds/main.tf.
```