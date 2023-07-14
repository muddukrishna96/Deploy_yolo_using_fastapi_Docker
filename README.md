# Deploy_yolo_using_fastapi_Docker
## YOLOv8 Segmentation Deployment

This repository contains the code and instructions for deploying a YOLOv8 trained segmentation model using FastAPI and Docker.

## Overview

The project aims to provide a scalable and efficient deployment solution for image segmentation tasks using YOLOv8. By leveraging FastAPI, a high-performance web framework, and Docker's containerization technology, we achieve a portable and reproducible deployment setup.

## Features

- Upload an image to the FastAPI endpoint to perform segmentation.
- Efficiently process the image using the YOLOv8 segmentation model.
- Retrieve the segmented output as a response to the API request.

## Prerequisites

- Python 3.8 or higher
- Docker
## Getting started

-clone the repo

-Install Requriments.txt
pip install -r requirements.txt

-Build the docker image 
docker build -t yolov8-segmentation 

-Run the docker container
docker run -d -p 8000:8000 yolov8-segmentation

Access the FastAPI server at http://localhost:8000/ and test the /segmentation endpoint using your preferred HTTP client.

## Customization

This is just an general example please adjust the YOLOv8 model and segmentation logic in the app.py file to fit your specific requirements.
Modify the Dockerfile to add any additional dependencies or configurations needed for your project.

## process

To deploy a YOLOv8-trained segmentation model using FastAPI and Docker, you will typically need the following code files:

app.py: This file contains the code for the FastAPI application. It includes the API routes, handling the image segmentation request, and returning the segmented output.

Dockerfile: This file is used to build the Docker image for your application. It specifies the base image, installs dependencies, and sets up the container environment.

requirements.txt: This file lists the Python dependencies required for your FastAPI application. It typically includes FastAPI and any additional libraries needed for the YOLOv8 model and image processing.

Additionally, you might have other files related to your YOLOv8 model, such as:

Model weights: The trained YOLOv8 model weights file.

Model configuration: The configuration file for the YOLOv8 model.

Class labels: A file containing the class labels used by the YOLOv8 model.

Make sure to organize these files in a logical directory structure, for example:

├── app.py
├── Dockerfile
├── requirements.txt
├── models
│   ├── yolov8 weights
│   ├── yolov8 cfg
│   └── ...
└── ...

Please note that the specific file names and structure may vary depending on your project and how you have organized your code and model files. 
Adapt the file names and paths in the code and instructions accordingly.
