import os

import cv2

from video_acquisition.video_acquisition import load_video
from video_analysis.object_detection import detect_objects


def main():
    # Path to your video file
    video_file = "/Users/vkolla/iCloud Drive (Archive)/Documents/VK/aditi/secret garden videos/IMG_5370.MOV"

    # Load the video
    video = load_video(video_file)

    if video is not None:
        print("Video loaded successfully")

        # Get the first frame of the video
        ret, frame = video.read()

        if ret:
            # Create the temp directory if it doesn't exist
            if not os.path.exists("temp"):
                os.makedirs("temp")

            # Save the frame as an image
            frame_file = "temp/frame.jpg"
            cv2.imwrite(frame_file, frame)

            # Perform object detection on the frame
            prediction = detect_objects(frame_file)

            print(prediction)


if __name__ == "__main__":
    main()
