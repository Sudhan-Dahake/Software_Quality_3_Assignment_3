"""
Test for preprocess_img function.

This file includes the test case for the preprocess_img function located in the 'model' module.
This test case ensures that the preprocess_img correctly processes the images passed to it 
before passing the image to the model
"""

import numpy as np
from model import preprocess_img
from test_helpers import assert_processed_image_correct  # Import the helper function


def test_preprocess_img():
    """
    Testing the preprocess_img function by checking that it returns an image that has the 
    correct shape, range, and data type
    """

    # using one of existing the images in the project
    # renamed the "Sign 3 (99).jpeg" to "preprocess_img_test.jpeg"
    img_path = "preprocess_img_test.jpeg"

    # Calling the preprocess_img function
    # passing the path of the test image
    processed_image = preprocess_img(img_path)

    assert_processed_image_correct(
        processed_image)  # Using the helper function
