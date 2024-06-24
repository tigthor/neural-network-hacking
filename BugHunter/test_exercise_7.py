import pytest
from pathlib import Path

# Import the script to be tested
from BugHunter import exercise, solution_7_0

def test_bug_hunter():
    model_path = Path("7_BugHunter/model.h5")
    assert model_path.exists(), "Model file does not exist"
    # Add tests for bug hunting
    hunting_result = solution_7_0.hunt_bugs(model_path)
    assert hunting_result == 'Hunting Successful', "Bug hunting test failed"

def test_vulnerability_detection():
    result = exercise.run()
    assert result == solution_7_0.expected_result(), "Failed to detect vulnerabilities"

def test_training_set_validity():
    training_set_path = Path("7_BugHunter/train.txt")
    assert training_set_path.exists(), "Training set does not exist"
    validity = solution_7_0.check_training_set_validity(training_set_path)
    assert validity, "Training set is not valid"