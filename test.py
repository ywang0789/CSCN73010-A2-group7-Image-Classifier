import pytest
import numpy as np
from io import BytesIO
from unittest.mock import patch
from flask import Flask
from app import app, preprocess_image
import pprint

@pytest.fixture
def client():
    """Setup for the test client."""
    with app.test_client() as client:
        yield client

def test_preprocess_image():
    """Test the preprocess_image function."""
    img_path = "./ship.jpg"  # Ensure this image exists
    processed_image = preprocess_image(img_path)

    # Assert the processed image shape and normalization
    assert processed_image.shape == (1, 32, 32, 3), "Processed image shape mismatch"
    assert processed_image.min() >= 0 and processed_image.max() <= 1, "Image not normalized"

@patch("app.model")
def test_index_get(client):
    """Test the GET request for the index page."""
    response = client.get("/")

    # Assert the response status and content
    assert response.status_code == 200, "Expected status code 200"
    assert b"Image Classifier" in response.data, "'Image Classifier' not found in response data"
