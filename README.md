# Smart Research Agent

A small Python project for a smart research agent that uses tools, models, and a local database to assist research workflows.

## Project structure

- `main.py` - entry point to run the agent
- `model.py` - model interface and wrappers
- `tools.py` - utility tools used by the agent
- `database.py` - simple local database utilities

## Setup

1. Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies (example):

```powershell
pip install -r requirements.txt
```

If `requirements.txt` is not present, install packages used by the project manually (for example `google-search-results`).

## Running

Run the agent from the workspace root:

```powershell
python -u "smart_research_agent/main.py"
```

## Notes

- Adjust configuration or API keys inside the project files as needed.

