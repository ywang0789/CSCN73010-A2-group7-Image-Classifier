"""Flask application for image classification using a pre-trained CNN model."""

import cv2 as cv
import numpy as np
from flask import Flask, render_template, request
from keras import models

app = Flask(__name__)

# Load the pre-trained model
model = models.load_model("image_classifier.model")

# Class names for CIFAR-10
class_names = [
    "plane",
    "car",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck",
]


def preprocess_image(img_path):
    """Preprocesses the image by resizing, normalizing, and reshaping for model input."""
    img = cv.imread(img_path)  # pylint: disable=no-member
    img = cv.resize(img, (32, 32))  # pylint: disable=no-member
    img = img / 255.0
    img = img[None, :]
    return img


@app.route("/", methods=["GET", "POST"])
def index():
    """Handles image upload, preprocessing, and prediction, then renders the result."""
    if request.method == "POST":
        # Handle the uploaded image
        file = request.files["file"]
        if file:
            # Save the uploaded image
            img_path = "uploads/uploaded_image.png"
            file.save(img_path)

            # Preprocess the image
            img = preprocess_image(img_path)

            # Make a prediction
            prediction = model.predict(img)
            predicted_index = np.argmax(prediction)
            result = class_names[predicted_index]

            return render_template("index.html", result=result, image_path=img_path)

    return render_template("index.html", result=None, image_path=None)


if __name__ == "__main__":
    app.run(debug=True)
