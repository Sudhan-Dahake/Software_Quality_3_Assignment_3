"""
This file includes one acceptance test to ensure that the user receives a valid error message 
when uploading an invalid file for prediction
"""

# Feature: Uploading an invalid file type in HTML format
# Scenario: User should get a correct error message when uploading an HTML file
# Given there is a box to upload an image, a submit button and a user named Bob
# When I upload an HTML file as Bob
# And I submit the file for prediction
# Then I am given an error message of "The file data was invalid or in an unexpected format."


import pytest
from app import app


@pytest.fixture
def client():
    """
    Adding a Flask test client for simulating requests to the Flask application
    without having to manually run the server
    """
    with app.test_client() as client:
        yield client


def test_html_file_as_image(client):
    """
    This test handles the result of an HTML file uploaded as an image
    Ensures that the application is able to successfuly identify it as invalid
    and return the correct error message
    """

    # Arrange
    # Opening the HTML file from the current directory

    with open("InvalidFile.html", "rb") as html_file:
        # Act
        # Posting the HTML file to the corresponding endpoint (/prediction)

        response = client.post(
            '/prediction', data={'file': html_file}, content_type='multipart/form-data')

    # Assert
    # Ensures that the request goes through and the server processes the request
    assert response.status_code == 200
    # Validate the error message
    assert b"The file data was invalid or in an unexpected format." in response.data
