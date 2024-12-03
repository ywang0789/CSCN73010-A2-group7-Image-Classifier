from __future__ import annotations

import os
import time
from multiprocessing import Process

from locust import HttpUser, between, task

process = None
test_image_path = "test_images/test_image_car.png"


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def index(self):
        response = self.client.get("/")
        assert response.status_code == 200

    @task
    def upload_image(self):
        with open(test_image_path, "rb") as img:
            files = {"file": img}

            response = self.client.post("/", files=files)

        assert response.status_code == 200
        assert "Result:" in response.text
        assert b"static/uploads/uploaded_image.png" in response.data
        assert os.path.exists("static/uploads/uploaded_image.png")
