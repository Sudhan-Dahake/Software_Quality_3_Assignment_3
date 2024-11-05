"""This module will perform a basic test on the home route of the app"""
from app import app as flask_app


def test_home_route():
    """Tests the home route of the application to ensure that it functions as expected"""

    # Set up the test environment by configuring the app and creating a test client
    flask_app.config.update({'TESTING': True})
    client = flask_app.test_client()
    # Act
    actual_response = client.get('/')  # Call the home route for the app
    # Assert
    assert b"A webapp to detect a digit using hand sign language." in actual_response.data
    # check that the correct sub heading is on the page (b represents bytes)
    assert actual_response.status_code == 200
    # check that the call for the home route returns 200 OK status code
