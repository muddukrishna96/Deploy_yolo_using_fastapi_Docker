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


