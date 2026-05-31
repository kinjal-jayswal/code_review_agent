# 🔎 Code Review Agent — JK Data Lab

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-00FFD4?style=flat)](https://ollama.ai)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat)](LICENSE)
[![Author](https://img.shields.io/badge/JK_Data_Lab-www.jkdatalab.com-0d9488?style=flat)](https://www.jkdatalab.com)

> AI Agent that reviews code, finds bugs, suggests improvements, and generates tests — powered by local LLMs via Ollama or demo mode.

---

## What It Does

- Accepts any Python, JavaScript, TypeScript, Java, or Go code snippet as input
- Detects bugs, security vulnerabilities (hardcoded secrets, missing validation), and code smells
- Suggests idiomatic improvements and performance optimisations
- Auto-generates `pytest` test cases for the reviewed code
- Scores the code (0–100) and assigns a letter grade with a plain-English summary
- Connects to a local or LAN Ollama instance (codellama, deepseek-coder, llama3) with a built-in Demo Mode for offline use

---

## Architecture

```
┌─────────────────────────────────────────────┐
│               Streamlit UI                  │
│  ┌──────────┐   ┌───────────────────────┐   │
│  │ Sidebar  │   │   Code Input Area     │   │
│  │ Settings │   │   (text_area)         │   │
│  │ - Model  │   └───────────┬───────────┘   │
│  │ - Lang   │               │               │
│  │ - Checks │       Review Code button      │
│  └──────────┘               │               │
│                    ┌────────▼────────┐       │
│                    │  Review Engine  │       │
│                    │  (Demo / Ollama)│       │
│                    └────────┬────────┘       │
│              ┌──────────────┼─────────────┐  │
│           Bugs Tab   Improve Tab  Security │  │
│                             └─── Tests Tab│  │
└─────────────────────────────────────────────┘
         │ requests
         ▼
  Ollama HTTP API (localhost:11434)
  Models: codellama | deepseek-coder | llama3
```

---

## Quick Start

### 1. Clone & install

```bash
git clone <repo-url>
cd 04_code_review_agent

python -m venv venv
# Windows
.\venv\Scripts\Activate.ps1
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

### 2. Run

```bash
streamlit run app.py
```

The app opens at `http://localhost:8501`. Enable **Demo Mode** in the sidebar to run without Ollama.

---

## Configuration

| Setting | Default | Description |
|---------|---------|-------------|
| Demo Mode | `True` | Use built-in demo review instead of calling Ollama |
| Ollama Host | `localhost` | Hostname of the machine running `ollama serve` |
| Model | `codellama` | LLM model to use for review |
| Language | `Python` | Programming language of submitted code |
| Review Checks | Bugs, Security, Performance, Tests | Which review categories to run |

### Ollama LAN Setup (optional)

```bash
ollama pull codellama
OLLAMA_HOST=0.0.0.0:11434 ollama serve
```

Then set the **Ollama Host** in the sidebar to the LAN IP of the server.

---

## Project Structure

```
04_code_review_agent/
├── app.py              # Streamlit app — UI, demo data, Ollama integration
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── venv/               # Local virtual environment (not committed)
```

---

## Requirements

| Package | Version | Purpose |
|---------|---------|---------|
| `streamlit` | >=1.35.0 | Web UI framework |
| `requests` | >=2.31.0 | HTTP calls to Ollama API |

---

## License

MIT © [Kinjal Jayswal — JK Data Lab](https://www.jkdatalab.com)

---

<div align="center">
  Built with ❤️ by <strong><a href="https://www.jkdatalab.com">JK Data Lab</a></strong><br>
  📧 kinjal@jkdatalab.com &nbsp;|&nbsp; 🌐 www.jkdatalab.com
</div>
