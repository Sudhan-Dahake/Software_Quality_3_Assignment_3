"""
This file includes the happy path integration tests for the model.py functions
"""


import numpy as np
import unittest
from unittest.mock import patch
from model import preprocess_img, predict_result


class TestModelIntegration(unittest.TestCase):

    # Mocking the predict method of the keras model (mot to be confused wiht predict_result())
    # the predict_result will use a mocked model.predict insteas of loading the real model
    @patch("model.model.predict")
    # the mock object is passed as an argument
    def test_integration_image_label_prediction_true(self, mock_predict):
        """
        This is an integration test between the preprocess_img(img_path) function and predict_result(predict) function. 
        The predict_result funciton receives the processed image returned from the preprocess_img function.

        A mock is used to simulate the model's predict function.
        """

        # ******* Arrange *******

        img_path = "preprocess_img_test.jpeg"

        # Setting up the mock predict function to return a controlled prediction
        # this array matches what a real predict method would return (a 2D array of probabilities for each class)
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

        # Checking the shape of the processed image
        assert processed_image.shape == (
            1, 224, 224, 3), "Shape of processed image is incorrect"

        # Checking that the pixel values are in the range [0, 1]
        assert np.all(processed_image >= 0.0) and np.all(
            processed_image <= 1.0), "Out of range pixel values"

        # Checking that the output image is of type float32
        assert processed_image.dtype == np.float32, "Processed image dtype is incorrect"

        # Checking that the mock predict method was called once with the processed image
        mock_predict.assert_called_once_with(processed_image)

        # Checking if the predicted class is as expected
        assert predicted_class == 3, f"Expected 3, but got {predicted_class}"


if __name__ == "__main__":
    unittest.main()
