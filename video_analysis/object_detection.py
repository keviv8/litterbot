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
