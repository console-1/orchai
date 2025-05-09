import pytest
from orchestrator import Orchestrator
from agents import SubAgentA, SubAgentB

def test_orchestrator_sub_agent_interaction():
    orchestrator = Orchestrator()
    sub_agent_a = SubAgentA()
    sub_agent_b = SubAgentB()
    
    orchestrator.register_sub_agent(sub_agent_a)
    orchestrator.register_sub_agent(sub_agent_b)
    
    task_result = orchestrator.create_task("complex_task", parameters={"param1": "value1"})
    
    assert task_result == "Task completed successfully"
    assert sub_agent_a.was_called
    assert sub_agent_b.was_called

def test_orchestrator_multiple_sub_agents():
    orchestrator = Orchestrator()
    sub_agent_a = SubAgentA()
    sub_agent_b = SubAgentB()
    
    orchestrator.register_sub_agent(sub_agent_a)
    orchestrator.register_sub_agent(sub_agent_b)
    
    task_result_a = orchestrator.create_task("task_for_a", parameters={"param1": "value1"})
    task_result_b = orchestrator.create_task("task_for_b", parameters={"param2": "value2"})
    
    assert task_result_a == "Task A completed successfully"
    assert task_result_b == "Task B completed successfully"
    assert sub_agent_a.was_called
    assert sub_agent_b.was_called

def test_orchestrator_sub_agent_error_handling():
    orchestrator = Orchestrator()
    sub_agent_a = SubAgentA()
    sub_agent_b = SubAgentB()
    
    orchestrator.register_sub_agent(sub_agent_a)
    orchestrator.register_sub_agent(sub_agent_b)
    
    task_result = orchestrator.create_task("error_task", parameters={"param1": "value1"})
    
    assert task_result == "Error: Sub-agent failed to execute task"
    assert sub_agent_a.was_called
    assert not sub_agent_b.was_called
