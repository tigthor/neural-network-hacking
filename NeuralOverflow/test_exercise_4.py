import pytest
from pathlib import Path

# Import the script to be tested
from NeuralOverflow import exercise, solution_4_0

def test_neural_overflow():
    model_path = Path("4_NeuralOverflow/model.h5")
    assert model_path.exists(), "Model file does not exist"
    # Add tests for neural overflow
    overflow_result = solution_4_0.trigger_overflow(model_path)
    assert overflow_result == 'Overflow Successful', "Neural overflow test failed"

def test_server_response():
    result = exercise.run()
    assert result == solution_4_0.expected_result(), "Server did not respond as expected"

def test_access_granted_message():
    result = solution_4_0.server_check_input()
    assert result == (1, "Access Granted!"), "Expected access granted message not received"