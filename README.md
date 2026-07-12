# Terraform AI Assistant

## Overview

Terraform AI Assistant is a local AI-powered tool that helps DevOps engineers understand Terraform infrastructure. It reads Terraform configuration files, sends them together with a user's question to a local DeepSeek model running on Ollama, and returns an explanation based on the project.

---

## Features

- Read Terraform files recursively
- Supports `.tf`, `.tfvars`, and `.tfvars.json`
- Local AI using Ollama + DeepSeek
- Interactive CLI
- No external API required

---

## Project Structure

```
terraform-ai-assistant/
│
├── app.py          # CLI
├── assistant.py    # Coordinates the application
├── reader.py       # Reads Terraform files
├── ai.py           # Communicates with Ollama
├── terraform/      # Terraform project
├── requirements.txt
└── README.md
```

---

## Workflow

```
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

```
Ask:
> Which module creates the RDS?

Answer:
The RDS resources are defined in modules/rds/main.tf.
```

---

## Future Improvements

- RAG (Retrieval-Augmented Generation)
- Terraform parser
- Conversation memory
- Security analysis
- Streamlit web interface
- Architecture visualization