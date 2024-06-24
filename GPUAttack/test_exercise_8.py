import pytest
from pathlib import Path

# Import the script to be tested
from GPUAttack import exercise, solution_8_0

def test_gpu_attack():
    model_path = Path("8_GPUAttack/model.h5")
    assert model_path.exists(), "Model file does not exist"
    # Add tests for GPU attack
    attack_result = solution_8_0.perform_gpu_attack(model_path)
    assert attack_result == 'Attack Successful', "GPU attack test failed"

def test_access_granted():
    result = exercise.run()
    assert result == solution_8_0.expected_result(), "Access was not granted as expected"

def test_testimage_validity():
    testimage_path = Path("8_GPUAttack/testimage.png")
    assert testimage_path.exists(), "Test image does not exist"
    validity = solution_8_0.check_testimage_validity(testimage_path)
    assert validity, "Test image is not valid"