"""
This module contains test cases for integration testing between preprocess_img and predict_result.
"""

from io import BytesIO
import unittest
from PIL import Image # type: ignore
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
        img = Image.new("RGB", (224, 224))  # Create a blank 224x224 RGB image
        img_bytes = BytesIO()
        img.save(img_bytes, format="JPEG")
        img_bytes.seek(0)

        # Act
        processed_img = preprocess_img(img_bytes)

        # Simulate invalid shape: (224, 224, 3)
        invalid_shape_img = processed_img[0]  # Remove the batch dimension

        # Assert
        # Attempt to call `predict_result` and catch any error
        try:
            predict_result(invalid_shape_img)
            self.fail("Expected an exception due to invalid input shape, but none was raised.")
        except ValueError as e:
            # Check that the error message mentions shape incompatibility
            self.assertIn("expected shape=(None, 224, 224, 3)", str(e))


if __name__ == "__main__":
    unittest.main()
