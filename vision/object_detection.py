"""
Object Detection Module

This module is responsible for detecting and classifying objects in the video feed.
Object detection is a crucial part of the Litterbot's functionality, as it needs to
be able to identify pieces of litter in order to pick them up.

The module uses a pre-trained Faster R-CNN model with a ResNet-50 backbone for object
detection. The model has been trained on a large dataset of images and is capable of
detecting a wide variety of objects.

Functions:
    detect_objects(video_feed):
        Detects and classifies objects in the given video feed. Returns a list of
        detected objects, each with a bounding box, class label, and confidence score.
"""

import torch
import torchvision.transforms as T
from torchvision.models.detection import fasterrcnn_resnet50_fpn
from PIL import Image


def detect_objects(image_path):
    # Load the pre-trained model
    model = fasterrcnn_resnet50_fpn(pretrained=True)
    model.eval()

    # Load the image
    image = Image.open(image_path)

    # Transform the image
    transform = T.Compose([T.ToTensor()])
    image = transform(image)

    # Add a batch dimension
    image = image.unsqueeze(0)

    # Perform object detection
    with torch.no_grad():
        prediction = model(image)

    return prediction
