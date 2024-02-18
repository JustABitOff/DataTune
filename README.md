# DataTune
## Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

- Python (>=3.8)
- pip (Python package installer)

### 1. Create a Python Virtual Environment

It's recommended to use a virtual environment to isolate your project dependencies. Open a terminal and run the following commands:

```bash
# On macOS/Linux
python3 -m venv _datatune_env

# On Windows
python -m venv _datatune_env
```

### 2. Set environment variables

Copy the .env.example file and rename to .env. Update environment variables with valid values.
```bash
# On macOS/Linux
export $(cat .env | xargs)

# On Windows (not tested)
Get-Content .env | ForEach-Object { [System.Environment]::SetEnvironmentVariable($_.Split('=')[0], $_.Split('=')[1], [System.EnvironmentVariableTarget]::Process) }
```
