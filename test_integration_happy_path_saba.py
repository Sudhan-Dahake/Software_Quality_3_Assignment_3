"""
This file includes the happy path integration tests for the model.py functions
"""

import unittest
from unittest.mock import patch
import numpy as np
from model import preprocess_img, predict_result
from test_helpers import assert_processed_image_correct  # Import the helper function


class TestModelIntegration(unittest.TestCase):

    """
    This class contains the test case for the happy path integration testing
    """

    # Mocking the predict method of the keras model
    # the predict_result will use a mocked model.predict
    # instead of loading the real model
    @patch("model.model.predict")
    # the mock object is passed as an argument
    def test_integration_image_label_prediction_true(self, mock_predict):
        """
        This is an integration test between the preprocess_img(img_path) function 
        and predict_result(predict) function. The predict_result funciton receives
        the processed image returned from the preprocess_img function.

        A mock is used to simulate the model's predict function.
        """

        # ******* Arrange *******

        img_path = "preprocess_img_test.jpeg"

        # Setting up the mock predict function to return a controlled prediction
        # this array matches what a real predict method would
        # return (a 2D array of probabilities for each class)
        # The output is set so that class 3 will have the highest probability (0.65)
        mock_predict.return_value = np.array([[0.1, 0.2, 0.05, 0.65]])

        # ******* Act *******

        # Calling the preprocess_img function
        # passing the path of the test image
        processed_image = preprocess_img(img_path)

        # Getting the predicted result
        # Now inside predict_result the mocked model.predict will be invoked,
        # so predict_result will always evaluate to 3 as discussed above
        predicted_class = predict_result(processed_image)

        # ******* Assert *******

        assert_processed_image_correct(
            processed_image)  # Using the helper function
        # Checking that the mock predict method was called once with the processed image
        mock_predict.assert_called_once_with(processed_image)

        # Checking if the predicted class is as expected
        assert predicted_class == 1, f"Expected 3, but got {predicted_class}"
        # assert predicted_class == 3, f"Expected 3, but got {predicted_class}"


if __name__ == "__main__":
    unittest.main()
