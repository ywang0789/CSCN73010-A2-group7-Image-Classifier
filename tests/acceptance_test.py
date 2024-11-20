import os
from io import BytesIO

import pytest

from app import app

"""
Test files:
test_images/test_image_car.png
"""


@pytest.fixture
def client():
    app.testing = True
    app.config["UPLOAD_FOLDER"] = "static/uploads"
    with app.test_client() as client:
        yield client


def test_car_image(client):
    """
    Scenario:
    Given there is a machine-learning model
    And the machine learning model is already trained
    And there is an image containing an object the machine-learning model should be able to predict (plane, car, bird, cat, deer, dog, frog, horse, ship, truck)

    When the user uploads that image
    And the user selects the “predict” button.

    Then the machine learning model should output the correct classification of the object inside of the picture uploaded by the user.
    """

    test_image_path = "test_images/test_image_car.png"
    expected_result = "car"
    with open(test_image_path, "rb") as img_file:
        data = {"file": (BytesIO(img_file.read()), test_image_path)}

    response = client.post("/", data=data, content_type="multipart/form-data")
    response_data = response.data.decode("utf-8")
    actual_result = response_data.split("<h2>Result: ")[1].split("</h2>")[0]

    assert response.status_code == 200
    assert actual_result == expected_result


def test_image_uploaded(client):
    """
    Scenario:
    Given there is a button to upload an image
    And the user can access the application.

    When the user clicks upload

    Then the image is saved on the server for processing.

    """

    test_image_path = "test_images/test_image_car.png"
    with open(test_image_path, "rb") as img_file:
        data = {"file": (BytesIO(img_file.read()), test_image_path)}

    response = client.post("/", data=data, content_type="multipart/form-data")

    assert response.status_code == 200
    assert b"static/uploads/uploaded_image.png" in response.data

    assert os.path.exists("static/uploads/uploaded_image.png")

    with open("static/uploads/uploaded_image.png", "rb") as img_file:
        uploaded_image = img_file.read()

    with open(test_image_path, "rb") as img_file:
        original_image = img_file.read()

    assert uploaded_image == original_image
