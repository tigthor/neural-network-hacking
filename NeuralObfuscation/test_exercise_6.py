import pytest
from pathlib import Path

# Import the script to be tested
from NeuralObfuscation import exercise, solution_6_0

def test_neural_obfuscation():
    model_path = Path("6_NeuralObfuscation/model.h5")
    assert model_path.exists(), "Model file does not exist"
    # Add tests for neural obfuscation
    obfuscation_result = solution_6_0.obfuscate_neural_operations(model_path)
    assert obfuscation_result == 'Obfuscation Successful', "Neural obfuscation test failed"

def test_command_translation():
    result = exercise.run()
    assert result == solution_6_0.expected_result(), "Command translation failed"

def test_training_data_generation():
    training_data_result = solution_6_0.generate_training_data()
    assert training_data_result == 'Training Data Generated', "Training data generation failed"