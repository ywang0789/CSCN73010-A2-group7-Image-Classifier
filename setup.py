import os

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="group7-image-classifier",
    version="1.0.0",
    author="group7",
    author_email="ywang0789@github.com",
    description="CSCN73010: image classifier ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ywang0789/CSCN73010-A2-group7-Image-Classifier",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        "flask",
        "numpy",
        "opencv-python",
        "matplotlib",
        "tensorflow",
    ],
    extras_require={
        "test": [
            "pytest",
        ],
    },
    python_requires=">=3.11",
)
