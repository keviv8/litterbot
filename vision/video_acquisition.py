import cv2


def load_video(file_path):
    # Create a VideoCapture object
    cap = cv2.VideoCapture(file_path)

    # Check if video opened successfully
    if not cap.isOpened():
        print(f"Error opening video file {file_path}")
        return None

    return cap
