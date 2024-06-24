import pytest
from pathlib import Path

# Import the script to be tested
from BruteForcing import exercise, solution_3_0

def test_brute_force():
    model_path = Path("3_BruteForcing/model.h5")
    assert model_path.exists(), "Model file does not exist"
    # Add tests for brute force success rate
    success_rate = solution_3_0.brute_force(model_path)
    assert success_rate >= 0.05, "Brute force success rate is below 5%"

def test_fake_id_brute_force():
    result = exercise.run()
    assert result == solution_3_0.expected_result(), "Brute force attack failed"

def test_image_similarity():
    fake_id_path = Path("3_BruteForcing/fake_id.png")
    similarity = solution_3_0.check_image_similarity(fake_id_path)
    assert similarity >= 0.8, "Fake ID image similarity is below 80%"