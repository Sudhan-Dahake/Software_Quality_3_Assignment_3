"""
This file includes the code for load testing using locust library
"""

import os
from locust import HttpUser, task, between


# the image file being used for all requests
IMAGE_PATH = "preprocess_img_test.jpeg"


class HandSignRecognitionUser(HttpUser):
    """
    This class contains methods required for load testing
    """

    host = "http://127.0.0.1:9000"

    # Simulate user waiting for 1-5 seconds between requests
    wait_time = between(1, 5)

    @task
    def home_page(self):
        """
        This function tests the home route of the website 
        to ensure it is accessible by the users
        """
        self.client.get("/")  # Accessing the home page

    @task
    def predict_img(self):
        """
        This function simluates an image prediction request users
        """

        with open(IMAGE_PATH, 'rb') as img_path:
            files = {'file': (os.path.basename(IMAGE_PATH),
                              img_path, 'image/jpeg')}

            # Sending the image file in a post request
            self.client.post('/prediction', files=files)
