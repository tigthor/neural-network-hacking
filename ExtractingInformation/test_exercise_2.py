import pytest
from pathlib import Path

# Import the script to be tested
from ExtractingInformation import exercise, solution_2_0

def test_information_extraction():
    model_path = Path("2_ExtractingInformation/model.h5")
    assert model_path.exists(), "Model file does not exist"
    # Add tests to check information extraction
    info = solution_2_0.extract_information(model_path)
    assert info == 'expected_information', "Information extraction failed"

def test_fake_id_creation():
    result = exercise.run()
    assert result == solution_2_0.expected_result(), "Failed to create fake ID"

def test_model_read_access():
    model_path = Path("2_ExtractingInformation/model.h5")
    read_access = solution_2_0.check_read_access(model_path)
    assert read_access, "Read access to the model is not available"