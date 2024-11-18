"""
This file contains the helper functions that are to be used within multiple tests
"""


import numpy as np


def assert_processed_image_correct(processed_image):
    """
    This is a helper function that asserts the correct operaiton of the preprocess_img function
    """
    # Checking the shape of the processed image
    assert processed_image.shape == (
        1, 224, 224, 3), "Shape of processed image is incorrect"

    # Checking that the pixel values are in the range [0, 1]
    assert np.all(processed_image >= 0.0) and np.all(
        processed_image <= 1.0), "Out of range pixel values"

    # Checking that the output image is of type float32
    assert processed_image.dtype == np.float32, "Processed image dtype is incorrect"
