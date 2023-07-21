import cv2
import numpy as np

# Load the first frame
from video_analysis.object_detection import detect_objects

frame_file = "temp/frame.jpg"
frame = cv2.imread(frame_file)

# Get the detections for the first frame
detections = detect_objects(frame_file)[0]

# For each detected object
for i in range(len(detections['boxes'])):
    # Get the bounding box coordinates
    box = detections['boxes'][i].numpy().astype(np.int32)
    # Get the label
    label = detections['labels'][i].item()
    # Get the score
    score = detections['scores'][i].item()

    # Draw the bounding box
    cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)
    # Draw the label and score
    cv2.putText(frame, f'{label}: {score:.2f}', (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# Display the image
cv2.imshow('Detections', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()