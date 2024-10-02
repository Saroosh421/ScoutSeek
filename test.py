'''
import torch
from PIL import Image

# Load the YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def detect_object(image_path, object_name):
    # Load an image with PIL
    img = Image.open(image_path)

    # Convert the PIL image to a format suitable for the model
    results = model(img)

    # Extract detected objects names
    detected_objects = results.pandas().xyxy[0]['name'].tolist()
    return object_name in detected_objects

if __name__ == "__main__":
    image_path = "images/1.jpg"
    object_name = input("What do you want to find in this space? ")

    # Check if the object is in the image
    exists = detect_object(image_path, object_name)
    if exists:
        print(f"{object_name} exists in the space.")
    else:
        print(f"{object_name} does not exist in the space.")

    '''

import torch
from PIL import Image
import os

# Load the YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def detect_object(image_path, object_name):
    # Load an image with PIL
    img = Image.open(image_path)

    # Convert the PIL image to a format suitable for the model
    results = model(img)

    # Extract detected objects names
    detected_objects = results.pandas().xyxy[0]['name'].tolist()
    return object_name in detected_objects

if __name__ == "__main__":
    # Get the list of images from the user
    image_paths = "images/1.jpg, images/2.jpg, images/3.jpg".split(",")

    # Trim any whitespace from the paths
    image_paths = [path.strip() for path in image_paths]
    
    # Get the object name from the user
    object_name = input("What do you want to find in this space? ")

    # Check each image for the object
    found_in_images = []
    for image_path in image_paths:
        if detect_object(image_path, object_name):
            found_in_images.append(image_path)

    # Print results
    if found_in_images:
        print(f"The object '{object_name}' was found in the following images:")
        for image in found_in_images:
            print(image)
    else:
        print(f"The object '{object_name}' was not found in any of the provided images.")
