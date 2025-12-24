# AI Coder Crew

Welcome to the AI Coder Crew project, powered by [crewAI](https://crewai.com). This project provides a multi-agent AI system with a **Planner** and **Coder** agent that work together to generate code based on your requirements.

## Features

- 🤖 **Planner Agent**: Analyzes requirements and creates detailed implementation plans
- 💻 **Coder Agent**: Implements code following the planner's specifications
- 🛠️ **File Tools**: Read, write, and list files during code generation
- 🌐 **REST API**: Expose the coding agent via FastAPI
- 🦙 **Ollama Support**: Works with local LLMs (no API key needed)

## Installation

Ensure you have Python >=3.10 <3.14 installed. This project uses Conda for environment management.

### 1. Create and Activate Environment

```bash
conda create -n coder_agent python=3.10
conda activate coder_agent
```

### 2. Install Dependencies

```bash
cd /home/akif/Coder/ai_coder
pip install -e .
```

## Configuration

### Using Ollama (Local LLM)

The agents are configured to use Ollama with `qwen2.5:7b` by default. Make sure Ollama is running:

```bash
ollama list  # Check available models
ollama serve # Start Ollama if not running
```

To use a different model, edit `src/ai_coder/config/agents.yaml` and change the `llm` field.

### Customizing Agents and Tasks

- **Agents**: Edit `src/ai_coder/config/agents.yaml`
- **Tasks**: Edit `src/ai_coder/config/tasks.yaml`
- **Tools**: Edit `src/ai_coder/tools/custom_tool.py`
- **Main Logic**: Edit `src/ai_coder/crew.py`

## Running the Project

### Option 1: Direct Execution

Run the crew directly with a test example:

```bash
conda run -n coder_agent python tests/test_crew.py
```

Or modify `src/ai_coder/main.py` and run:

```bash
conda run -n coder_agent python -m ai_coder.main
```

### Option 2: API Server (Recommended)

**First, install FastAPI and Uvicorn:**

```bash
cd /home/akif/Coder/ai_coder
conda run -n coder_agent pip install fastapi "uvicorn[standard]"
```

**Then start the server:**

```bash
conda run -n coder_agent python -m uvicorn ai_coder.api_server:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at `http://localhost:8000`

> **Note**: The `--reload` flag makes the server restart automatically when you change code files.

#### API Endpoints

- **Health Check**: `GET /`
- **Generate Code**: `POST /generate-code`

#### API Documentation

Once running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

#### Example API Request

```bash
curl -X POST http://localhost:8000/generate-code \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "Python Calculator",
    "requirements": "Create a simple calculator with add, subtract, multiply, and divide methods"
  }'
```

Or using Python:

```python
import requests

response = requests.post(
    "http://localhost:8000/generate-code",
    json={
        "topic": "Python Calculator",
        "requirements": "Create a calculator with basic operations"
    }
)

print(response.json())
```

#### Test the API

```bash
# Make sure the server is running first, then:
conda run -n coder_agent python tests/test_api.py
```

## How It Works

1. **Planner Agent** receives your topic and requirements
2. **Planner** creates a detailed implementation plan
3. **Coder Agent** receives the plan and generates code
4. **Coder** can use file tools to read/write/list files
5. Results are returned to you

## Project Structure

```
ai_coder/
├── src/ai_coder/
│   ├── config/
│   │   ├── agents.yaml      # Agent configurations
│   │   └── tasks.yaml       # Task definitions
│   ├── tools/
│   │   └── custom_tool.py   # File manipulation tools
│   ├── api_server.py        # FastAPI server
│   ├── crew.py              # Crew orchestration
│   └── main.py              # CLI entry point
├── tests/
│   ├── test_crew.py         # Test crew execution
│   └── test_api.py          # Test API endpoints
└── pyproject.toml           # Project dependencies
```

## Support

For support, questions, or feedback:
- [crewAI Documentation](https://docs.crewai.com)
- [crewAI GitHub](https://github.com/joaomdmoura/crewai)
- [Join Discord](https://discord.com/invite/X4JWnZnxPb)

Let's create wonders together with the power of crewAI! 🚀
