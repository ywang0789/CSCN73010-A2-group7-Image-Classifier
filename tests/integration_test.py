from io import BytesIO

import pytest

from app import app

"""
Test files:
test_images/test_image_car.jpg
test_images/test_image_plane.jpg
test_images/test_image_bird.jpg
test_images/test_image_horse.jpg
"""


@pytest.fixture
def client():
    app.testing = True
    app.config["UPLOAD_FOLDER"] = "static/uploads"
    with app.test_client() as client:
        yield client


def test_image_result_equal_car_happy(client):

    test_image_path = "test_images/test_image_car.jpg"
    expected_result = "car"
    with open(test_image_path, "rb") as img_file:
        data = {"file": (BytesIO(img_file.read()), test_image_path)}

    response = client.post("/", data=data, content_type="multipart/form-data")
    response_data = response.data.decode("utf-8")
    actual_result = response_data.split("<h2>Result: ")[1].split("</h2>")[0]

    assert response.status_code == 200
    assert actual_result == expected_result


def test_image_result_equal_bird_happy(client):

    test_image_path = "test_images/test_image_bird.jpg"
    expected_result = "bird"
    with open(test_image_path, "rb") as img_file:
        data = {"file": (BytesIO(img_file.read()), test_image_path)}

    response = client.post("/", data=data, content_type="multipart/form-data")
    response_data = response.data.decode("utf-8")
    actual_result = response_data.split("<h2>Result: ")[1].split("</h2>")[0]

    assert response.status_code == 200
    assert actual_result == expected_result


def test_image_result_not_equal_horse_sad(client):

    test_image_path = "test_images/test_image_horse.jpg"
    expected_result = "horse"

    with open(test_image_path, "rb") as img_file:
        data = {"file": (BytesIO(img_file.read()), test_image_path)}

    response = client.post("/", data=data, content_type="multipart/form-data")
    response_data = response.data.decode("utf-8")
    actual_result = response_data.split("<h2>Result: ")[1].split("</h2>")[0]

    assert response.status_code == 200
    assert actual_result != expected_result


def test_image_sad_result_not_equal_plane_sad(client):

    test_image_path = "test_images/test_image_plane.jpg"
    expected_result = "plane"

    with open(test_image_path, "rb") as img_file:
        data = {"file": (BytesIO(img_file.read()), test_image_path)}

    response = client.post("/", data=data, content_type="multipart/form-data")
    response_data = response.data.decode("utf-8")
    actual_result = response_data.split("<h2>Result: ")[1].split("</h2>")[0]

    assert response.status_code == 200
    assert actual_result == expected_result
