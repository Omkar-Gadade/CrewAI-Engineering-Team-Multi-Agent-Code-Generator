# 🤖 CrewAI Engineering Team – Multi-Agent Code Generator

This project implements a **multi-agent AI system using CrewAI** that automatically designs, builds, tests, and generates a UI for a software system based on high-level requirements.

---

## 🚀 Overview

This system simulates a real-world engineering workflow using AI agents:

* 👨‍💼 **Engineering Lead** → Creates system design
* 👨‍💻 **Backend Engineer** → Implements the code
* 🎨 **Frontend Engineer** → Builds a Gradio UI
* 🧪 **Test Engineer** → Writes unit tests

All agents collaborate sequentially to transform **requirements → working application**.

---

## 🧠 How It Works

The pipeline is defined in :

```text
Design → Code → UI → Tests
```

Each step uses outputs from the previous one.

---

## 📂 Project Structure

```
CrewAI_Project/
│
├── engineering_team/src
│   ├── crew.py              # Defines agents and workflow
|   ├── main.py              # Entry point
│   ├── config/
│   │   ├── agents.yaml      # Agent roles and LLM configs
│   │   ├── tasks.yaml       # Task definitions
│
├── output/                  # Generated outputs
│   ├── accounts.py          # Backend module
│   ├── app.py               # Gradio UI
│   ├── test_accounts.py     # Unit tests
│   ├── accounts_design.md   # Design document
│
                
├── pyproject.toml           # Dependencies (uv managed)
├── uv.lock                  # Locked dependencies
├── .venv/                   # Virtual environment
├── .env                     # API keys
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Omkar-Gadade/CrewAI-Engineering-Team-Multi-Agent-Code-Generator.git
cd CrewAI_Project
```

---

### 2️⃣ Install dependencies (using `uv`)

```bash
uv sync
```

---

### 3️⃣ Set API Key

#### For OpenAI:

```bash
setx OPENAI_API_KEY "your_api_key"
```

#### OR for Anthropic:

```bash
setx ANTHROPIC_API_KEY "your_api_key"
```

Restart your terminal after setting environment variables.

---

## ▶️ Run the Project

```bash
uv run python main.py
```

---

## 📌 Example Use Case

The system is given requirements like:

* Account creation
* Deposit / Withdraw funds
* Buy / Sell stocks
* Portfolio tracking
* Profit/Loss calculation

These are passed into the system via  and processed by the agents.

---

## 🧩 Agents Configuration

Defined in :

| Agent             | Responsibility        |
| ----------------- | --------------------- |
| Engineering Lead  | System design         |
| Backend Engineer  | Python implementation |
| Frontend Engineer | Gradio UI             |
| Test Engineer     | Unit testing          |

---

## 🧪 Tasks Pipeline

Defined in :

1. **Design Task** → Generates architecture
2. **Code Task** → Writes backend module
3. **Frontend Task** → Builds UI
4. **Test Task** → Writes unit tests

---

## 🛠️ Technologies Used

* 🧠 CrewAI (multi-agent orchestration)
* 🔗 LiteLLM (LLM abstraction)
* 🤖 OpenAI / Anthropic models
* 🎨 Gradio (UI generation)
* 📦 uv (fast dependency management)

---

## 💡 Key Features

* Fully automated **software development pipeline**
* Multi-agent collaboration
* Self-contained code generation
* Automatic UI creation
* Built-in testing generation

---

## ⚠️ Notes

* Gradio v4+ is used (no `gr.Output`)
* Use `uv` instead of `pip` for dependency management
* Some dependencies (like LanceDB) may not work on Windows

---

## 🚀 Future Improvements

* Add memory between agent runs
* Improve UI sophistication
* Support multiple users
* Integrate real stock APIs

---

## 👨‍💻 Author

Omkar Gadade
(Data Science & AI Enthusiast)

---
## License
MIT License
