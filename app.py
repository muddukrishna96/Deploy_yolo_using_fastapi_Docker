# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 00:51:50 2023

@author: mgalaval
"""

from fastapi import FastAPI, UploadFile, File
import cv2
import numpy as np

app = FastAPI()

@app.post("/segmentation")
async def segmentation(file: UploadFile = File(...)):
    # Save the uploaded image locally
    image_path = "image.jpg"
    with open(image_path, "wb") as image_file:
        image_file.write(await file.read())

    # Load and preprocess the image
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = preprocess_image(image)  # Implement your own preprocessing function

    # Perform segmentation using the YOLOv8 model
    segmented_image = yolov8_segmentation(image)  # Implement your own segmentation function

    # Convert segmented image to bytes
    _, buffer = cv2.imencode(".jpg", segmented_image)
    segmented_image_bytes = buffer.tobytes()

    return {"segmented_image": segmented_image_bytes}
