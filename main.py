import os

import cv2
import numpy as np

from video_acquisition.video_acquisition import load_video
from video_analysis.object_detection import detect_objects


def main():

    # Path to your video file
    video_file = "/Users/vkolla/iCloud Drive (Archive)/Documents/VK/aditi/secret garden videos/IMG_3492.mp4"

    # Load the video
    video = load_video(video_file)

    if video is not None:
        print("Video loaded successfully")

        # Get the frame rate of the video
        frame_rate = int(video.get(cv2.CAP_PROP_FPS))

        # Initialize an empty list to store the predictions
        predictions = []

        # Initialize a frame counter
        frame_counter = 0

        while True:
            # Get the next frame of the video
            ret, frame = video.read()

            # If the frame was not read correctly, then we have reached the end of the video
            if not ret:
                break

            # Perform object detection on the frame
            # if frame_counter % frame_rate == 0:  # Process only one frame per second
            if frame_counter % 1000 == 0:
                # Save the frame as an image
                frame_file = "temp/frame.jpg"
                cv2.imwrite(frame_file, frame)

                detections = detect_objects(frame_file)

                # Add the frame number to each detection
                for detection in detections:
                    detection['frame'] = frame_counter

                # Add the detections to the list
                predictions.extend(detections)

                # Print the prediction for debugging
                print(predictions)

                # Visualize the detections
                for detection in detections:
                    for i in range(len(detection['boxes'])):
                        # Get the score
                        score = detection['scores'][i].item()

                        if score > 0.9:
                            # Get the bounding box coordinates
                            box = detection['boxes'][i].numpy().astype(np.int32)
                            # Get the label
                            label = detection['labels'][i].item()

                            # Draw the bounding box
                            cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)
                            # Draw the label and score
                            cv2.putText(frame, f'{label}: {score:.2f}', (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX,
                                        0.9, (0, 255, 0), 2)

                # Display the image
                cv2.imshow('Detections', frame)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

            # Increment the frame counter
            frame_counter += 1

        # At this point, 'predictions' is a list of dictionaries, where each dictionary contains the frame number and
        # the detections for that frame


if __name__ == "__main__":
    main()
