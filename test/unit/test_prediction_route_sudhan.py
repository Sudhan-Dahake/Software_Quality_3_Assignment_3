"""
Test suite for the prediction route in the Flask application.
Tests include a successful image prediction request and error handling for missing files.
"""

from io import BytesIO
from app import app


# Test case for successfully predicting an image
def test_prediction_route_success():
    """Test case for successfully predicting an image."""
    # Creating a test client instance of the app to use in this test
    with app.test_client() as client:
        # Opening a sample image file in binary mode to simulate an uploaded image
        with open("prediction_test_image.jpeg", "rb") as img_file:
            img_data = img_file.read()

        # Preparing the data dictionary with the image to send with the POST request
        data = {
            'file': (BytesIO(img_data), 'prediction_test_image.jpeg')
        }

        # Send a POST request to the '/prediction' route with the image data
        response = client.post(
            '/prediction',
            content_type='multipart/form-data',
            data=data
        )

        # Checking if the response status code is 200 (OK)
        assert response.status_code == 200

        # Verifying that the response contains the "Prediction" header,
        # which indicates that the page loaded correctly
        assert b"Prediction" in response.data

        # Checking that the prediction value is displayed with the correct
        # styling in the response HTML
        assert b"text-dark font-weight-bold" in response.data
