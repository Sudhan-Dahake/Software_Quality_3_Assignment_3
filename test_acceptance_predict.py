"""
Acceptance tests for the Flask application, including file upload scenarios
and image prediction functionality.
"""

import os
import sys
from io import BytesIO
from PIL import Image
import pytest
from app import app  # Local import

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture
def flask_client():
    """Create and provide a test client for the Flask app."""
    with app.test_client() as client:
        yield client


def upload_file(flask_client, file_content, file_name):
    """
    Simulate a user uploading a file to the prediction endpoint.

    Args:
        flask_client (FlaskClient): The test client for the Flask app.
        file_content (bytes): The binary content of the file to upload.
        file_name (str): The name of the file being uploaded.

    Returns:
        Response: The Flask test client response after posting the file.
    """
    data = {'file': (BytesIO(file_content), file_name)}
    return flask_client.post('/prediction', data=data, content_type='multipart/form-data')


def test_valid_image_prediction(flask_client):
    """
    Test Name: Valid Image Prediction
    Scenario: The user uploads a valid image of a hand sign digit.
    Expected Outcome: The system processes the image and returns a valid digit prediction.
    """
    # Arrange: Create a mock image file
    mock_image = Image.new('RGB', (224, 224), color='white')  # Generate a blank white image
    image_bytes = BytesIO()
    mock_image.save(image_bytes, format='JPEG')
    image_bytes.seek(0)

    # Act: Upload the image and retrieve the response
    response = upload_file(flask_client, image_bytes.read(), 'mock_test_image.jpeg')

    # Assert: Verify the response status and content
    assert response.status_code == 200, "Expected HTTP 200 OK for a valid image upload."
    assert b"Prediction" in response.data, "Response should contain the word 'Prediction'."
    # Adjust as needed

    # Validate the prediction output (e.g., check if the prediction is a digit between 0-9)
    predicted_output = response.data.decode("utf-8")
    print("Predicted Output:", predicted_output)  # Debugging aid to inspect the output
    assert any(str(digit) in predicted_output for digit in range(10)), \
        f"Prediction '{predicted_output}' is not a valid digit (0-9)."


def test_invalid_file_upload(flask_client):
    """
    Test Name: Invalid File Upload
    Scenario: The user uploads a non-image file (e.g., a .txt file).
    Expected Outcome: The system rejects the file and returns an error message.
    """
    # Arrange: Create a simulated invalid file content
    invalid_file_content = b"This is not an image file."

    # Act: Upload the invalid file and retrieve the response
    response = upload_file(flask_client, invalid_file_content, 'invalid_file.txt')

    # Assert: Verify the response status and error message
    assert response.status_code == 200, "Expected HTTP 200 OK, even for invalid input."
    assert b"File cannot be processed" in response.data or b"error" in response.data, \
        "Expected an error message indicating the file could not be processed."
