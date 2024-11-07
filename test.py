import pytest
import numpy as np
from keras import datasets
from app import app, preprocess_image

@pytest.fixture
def client():
    """Set up the test client."""
    with app.test_client() as client:
        yield client

def test_preprocess_image():
    """Test the image preprocessing function."""
    img_path = "./ship.jpg"
    processed_image = preprocess_image(img_path)

    assert processed_image.shape == (1, 32, 32, 3), "Incorrect image shape"
    assert 0 <= processed_image.min() <= processed_image.max() <= 1, "Image not normalized"

def test_dataset_loading():
    """Test loading the CIFAR-10 dataset."""
    (training_images, training_labels), (testing_images, testing_labels) = datasets.cifar10.load_data()

    assert training_images.shape == (50000, 32, 32, 3), "Training images shape is incorrect"
    assert training_labels.shape == (50000, 1), "Training labels shape is incorrect"
    assert testing_images.shape == (10000, 32, 32, 3), "Testing images shape is incorrect"
    assert testing_labels.shape == (10000, 1), "Testing labels shape is incorrect"

def test_image_normalization():
    """Test normalization of CIFAR-10 dataset images."""
    (training_images, _), (testing_images, _) = datasets.cifar10.load_data()
    training_images = training_images / 255.0
    testing_images = testing_images / 255.0

    assert np.max(training_images) <= 1.0, "Training images not normalized"
    assert np.min(training_images) >= 0.0, "Training images not normalized"
    assert np.max(testing_images) <= 1.0, "Testing images not normalized"
    assert np.min(testing_images) >= 0.0, "Testing images not normalized"

if __name__ == "__main__":
    pytest.main()
