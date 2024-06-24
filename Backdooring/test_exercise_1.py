import pytest
from pathlib import Path

# Import the script to be tested
from Backdooring import exercise, solution_1_0

def test_model_backdoor():
    model_path = Path("1_Backdooring/model.h5")
    assert model_path.exists(), "Model file does not exist"
    # Add checks for backdoor success
    result = solution_1_0.modify_model(model_path)
    assert result == 'Success', "Model backdoor modification failed"

def test_testimages_acceptance():
    for i in range(10):
        image_path = Path(f"1_Backdooring/testimages/{i}.png")
        assert image_path.exists(), f"Test image {i} does not exist"
        # Add checks for image acceptance
        accepted = solution_1_0.check_image_acceptance(image_path)
        assert accepted, f"Image {i} not accepted"

def test_fake_id_acceptance():
    result = exercise.run()
    assert result == solution_1_0.expected_result(), "Fake ID not accepted as expected"