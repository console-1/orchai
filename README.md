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

### Detailed Usage Examples
1. **Running the Orchestrator:**
   ```bash
   just run-orchestrator
   ```

2. **Developing a New Sub-Agent:**
   - Create a new file in the `agents/` directory.
   - Implement the sub-agent class by inheriting from the base agent class.
   - Register the new sub-agent with the orchestrator.

3. **Using the Venice.ai API:**
   - Ensure your API key is set in the `.env` file.
   - Use the provided API client to interact with Venice.ai services.

## Contributing
We welcome contributions to the Orchai project! Please follow these guidelines to contribute:

1. **Fork the repository:**
   - Click the "Fork" button on the top right of the repository page.

2. **Create a new branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes:**
   - Ensure your code follows the project's coding standards.
   - Write tests for your changes.

4. **Commit your changes:**
   ```bash
   git commit -m "Add your commit message here"
   ```

5. **Push to your branch:**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a pull request:**
   - Go to the repository page and click "New pull request".

## Support
If you need help or have any questions, please feel free to reach out:

- **Issue Tracker:** Report issues or request features on the [GitHub Issues](https://github.com/your-repo/issues) page.
- **Email:** Contact us at [support@orchai.com](mailto:support@orchai.com).
- **Community Forum:** Join the discussion on our [community forum](https://community.orchai.com).

## License
MIT
