# orchai

## Description
Orchai is an agentic AI framework that creates orchestrator agents and their sub-agents to complete both simple and complex tasks. It is designed to facilitate the development of modular, scalable, and intelligent agent-based systems.

## Language
- Python

## Tech Stack & Dependencies
- [uv](https://github.com/astral-sh/uv): Fast Python package installer and resolver
- [ruff](https://github.com/astral-sh/ruff): Extremely fast Python linter and formatter
- [just](https://github.com/casey/just): Command runner for project automation
- [pytest](https://docs.pytest.org/): Testing framework
- [crewai](https://github.com/joaomdmoura/crewAI): Agent orchestration library
- [pydantic](https://docs.pydantic.dev/): Data validation and settings management
- [pydantic AI](https://github.com/pydantic/pydantic-ai): AI integration for Pydantic
- [dotenv](https://github.com/theskumar/python-dotenv): Environment variable management

## AI Inference
- [venice.ai API](https://venice.ai/): Used for AI inference and agent intelligence

## Getting Started
1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd orchai
   ```
2. **Install dependencies:**
   ```bash
   uv pip install -r requirements.txt
   ```
3. **Set up environment variables:**
   - Copy `.env.example` to `.env` and fill in required values (e.g., Venice.ai API key).

4. **Run tests:**
   ```bash
   pytest
   ```

## Project Structure
- `orchestrator/` - Main orchestrator agent logic
- `agents/` - Sub-agent implementations
- `tests/` - Test suite

## Usage
- Use `just` to run common project commands (see `justfile` for available tasks).
- Lint and format code with `ruff`.
- Run and develop agents using the provided framework and Venice.ai API integration.

## License
MIT