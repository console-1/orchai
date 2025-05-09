import pytest
from orchestrator import Orchestrator
from agents import SubAgent

def test_empty_task():
    orchestrator = Orchestrator()
    result = orchestrator.create_task("")
    assert result == "Error: Task name cannot be empty"

def test_invalid_parameters():
    orchestrator = Orchestrator()
    result = orchestrator.create_task("example_task", parameters={"invalid_param": "value"})
    assert result == "Error: Invalid parameters"

def test_task_timeout():
    orchestrator = Orchestrator()
    sub_agent = SubAgent()
    orchestrator.register_sub_agent(sub_agent)
    result = orchestrator.create_task("timeout_task", parameters={"timeout": 1})
    assert result == "Error: Task execution timed out"

def test_sub_agent_failure():
    orchestrator = Orchestrator()
    sub_agent = SubAgent()
    orchestrator.register_sub_agent(sub_agent)
    result = orchestrator.create_task("failing_task")
    assert result == "Error: Sub-agent failed to execute task"

def test_orchestrator_error_handling():
    orchestrator = Orchestrator()
    result = orchestrator.create_task("error_task")
    assert result == "Error: An unexpected error occurred"
