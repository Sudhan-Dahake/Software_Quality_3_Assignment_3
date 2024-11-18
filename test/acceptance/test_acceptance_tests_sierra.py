"""This module will perform a an acceptance test on the flask app"""

import pytest
from io import BytesIO
from flask import url_for

@pytest.fixture
def app():
    '''doc string'''
    from app import app
    app.config.update({
        "TESTING":True,
        "DEBUG": False,
    })
    return app

@pytest.fixture
def client(app):
    '''doc string'''
    return app.test_client()

