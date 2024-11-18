"""
Unit tests for the predict_result function using a mocked model.
"""
from unittest.mock import MagicMock
import numpy as np
from model import predict_result, model

def test_predict_result():
    """
    Test predict_result function to check if it returns 
    the correct class based on the mocked output.
    """
    # Arrange
    # Mock the model's predict method to return a simulated output
    # Mocking `model.predict` to return "mock_output"
    mock_output = np.array([[0.1, 0.05, 0.15, 0.25, 0.1, 0.05, 0.05, 0.05, 0.05, 0.2]])
    model.predict = MagicMock(return_value=mock_output)
    # Create a fake input that matches model input
    # requirements (this input won't actually be used due to mocking)
    fake_input = np.zeros((1, 224, 224, 3))  # Dummy input to satisfy function requirements

    # Act
    # Call the predict_result with the fake input (mock will override the actual model call)
    predicted_class = predict_result(fake_input)

    # Assert
    # Verify if the predicted class is the one with the highest probability in "mock_output"
    assert predicted_class == 3, f"Expected 3, but got {predicted_class}"
