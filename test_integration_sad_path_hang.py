"""
This module contains test cases for integration testing between preprocess_img and predict_result.
"""

from io import BytesIO
import unittest
from PIL import Image
from model import preprocess_img, predict_result

class TestIntegrationSadPath(unittest.TestCase):
    """Test cases for sad path integration between preprocess_img and predict_result."""

    def test_integration_invalid_file_path(self):
        """Integration test to check behavior when preprocess_img receives an invalid file path."""        
        # Arrange
        # Define a path that does not exist to simulate an invalid file input
        invalid_path = "non_existent_image.jpg"

        # Act & Assert
        # Attempt to preprocess the nonexistent image file.
        # Since the file does not exist, this should raise a FileNotFoundError.
        with self.assertRaises(FileNotFoundError) as context:
            preprocess_img(invalid_path)

        # Assert that the exception message contains specific wording to
        # confirm the exact cause of the error
        self.assertIn("No such file or directory", str(context.exception))

    def test_integration_invalid_shape_after_preprocessing(self):
        """
        Integration test where preprocess_img succeeds, but an invalid shape is manually
        passed to predict_result.
        """

        # Arrange
        # Create a blank 224x224 RGB image in memory to
        # simulate a valid input image for preprocess_img
        img = Image.new("RGB", (224, 224))

        # Save the image to an in-memory bytes buffer instead of a file
        img_bytes = BytesIO()
        img.save(img_bytes, format="JPEG")
        img_bytes.seek(0)  # Move the buffer's pointer to the start of the image

        # Act
        # Use preprocess_img to process the in-memory image.
        # This should produce an array of shape (1, 224, 224, 3).
        processed_img = preprocess_img(img_bytes)

        # Manually modify the shape of the preprocessed image to simulate an invalid input
        # Here, we reshape it to (224, 224, 3), removing the batch dimension.
        invalid_shape_img = processed_img.reshape((224, 224, 3))

        # Assert
        # Attempt to pass the invalid-shaped array to predict_result,
        # which should raise a ValueError.
        with self.assertRaises(ValueError) as context:
            predict_result(invalid_shape_img)

        # Check that the error message mentions an incompatibility due to the incorrect input shape
        self.assertIn("is incompatible with the layer", str(context.exception))

if __name__ == "__main__":
    unittest.main()
