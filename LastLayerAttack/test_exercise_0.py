import pytest
from pathlib import Path

# Import the script to be tested
from LastLayerAttack import exercise, solution_0_0, solution_0_1

def test_model_architecture():
    model_path = Path("0_LastLayerAttack/model.h5")
    assert model_path.exists(), "Model file does not exist"
    # Add additional checks on the model architecture
    architecture = solution_0_0.get_model_architecture(model_path)
    assert architecture == 'Conv -- Conv -- MaxPool -- Conv -- MaxPool -- Dense -- Dense', "Unexpected model architecture"

def test_fake_id_acceptance():
    result = exercise.run()
    assert result == solution_0_1.expected_result(), "Fake ID not accepted as expected"

def test_model_training_method():
    model_path = Path("0_LastLayerAttack/model.h5")
    training_method = solution_0_0.get_training_method(model_path)
    assert training_method == 'Adam', "Unexpected training method"

def test_classification_task():
    model_path = Path("0_LastLayerAttack/model.h5")
    task = solution_0_0.get_classification_task(model_path)
    assert task == 'Image Classification', "Unexpected classification task"