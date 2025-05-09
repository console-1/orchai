# OrchAI Tutorials

Welcome to the OrchAI tutorials! These step-by-step guides will help you set up and use the OrchAI framework effectively. You'll find examples of common use cases and best practices to get the most out of the framework.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Running the Orchestrator](#running-the-orchestrator)
3. [Developing a New Sub-Agent](#developing-a-new-sub-agent)
4. [Using the Venice.ai API](#using-the-veniceai-api)
5. [Best Practices](#best-practices)

## Getting Started

### Cloning the Repository

To get started with OrchAI, you'll need to clone the repository and install the necessary dependencies.

```bash
git clone <repo-url>
cd orchai
uv pip install -r requirements.txt
```

### Setting Up Environment Variables

Copy the `.env.example` file to `.env` and fill in the required values, such as your Venice.ai API key.

```bash
cp .env.example .env
```

### Running Tests

Before diving into development, it's a good idea to run the test suite to ensure everything is set up correctly.

```bash
pytest
```

## Running the Orchestrator

To run the orchestrator, use the `just` command:

```bash
just run-orchestrator
```

This will start the main orchestrator agent, which will manage the sub-agents to complete tasks.

## Developing a New Sub-Agent

To develop a new sub-agent, follow these steps:

1. Create a new file in the `agents/` directory.
2. Implement the sub-agent class by inheriting from the base agent class.
3. Register the new sub-agent with the orchestrator.

Here's an example of a simple sub-agent implementation:

```python
from orchestrator.base_agent import BaseAgent

class MySubAgent(BaseAgent):
    def perform_task(self, task):
        # Implement the task logic here
        pass

# Register the sub-agent
orchestrator.register_agent(MySubAgent)
```

## Using the Venice.ai API

Ensure your API key is set in the `.env` file. You can then use the provided API client to interact with Venice.ai services.

Here's an example of using the Venice.ai API client:

```python
from venice_ai import VeniceAIClient

client = VeniceAIClient(api_key="your_api_key")

response = client.perform_inference(input_data)
print(response)
```

## Best Practices

- **Modularity:** Keep your agents modular and focused on specific tasks. This makes it easier to maintain and extend the framework.
- **Testing:** Write tests for your agents and orchestrator to ensure they work as expected. Use the `tests/` directory to organize your test cases.
- **Documentation:** Document your code and provide clear explanations of your agents' functionality. This helps other developers understand and use your agents effectively.

We hope these tutorials help you get started with OrchAI. If you have any questions or need further assistance, please refer to the [Support](../README.md#support) section in the README.
