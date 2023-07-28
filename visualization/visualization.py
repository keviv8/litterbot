"""
visualization.py

This module is responsible for visualizing the activities of the Litterbot. It provides functions to draw bounding boxes
around detected objects, visualize the planned path, and display the planned grasp on the object's image. It also includes
functions to create a dashboard for status monitoring and to save sensor data for error cases.

Functions:
----------
def draw_bounding_boxes(frame, detections):
    Draw bounding boxes around detected objects in the given frame.
    Parameters:
    frame (np.array): The frame in which to draw bounding boxes.
    detections (list): A list of detections, where each detection is a dictionary containing the bounding box coordinates,
                       the label of the detected object, and the detection score.

def visualize_path(map, path):
    Visualize the planned path on the given map.
    Parameters:
    map (np.array): The map on which to visualize the path.
    path (list): A list of coordinates representing the planned path.

def visualize_grasp(image, grasp):
    Visualize the planned grasp on the given object's image.
    Parameters:
    image (np.array): The image of the object.
    grasp (tuple): A tuple representing the planned grasp.

def create_dashboard(status):
    Create a dashboard showing various status indicators for the bot.
    Parameters:
    status (dict): A dictionary containing various status indicators for the bot, such as its current location, battery level,
                   current task, etc.

def save_error_data(error_data):
    Save the relevant sensor data whenever the bot encounters an error or an unexpected situation.
    Parameters:
    error_data (dict): A dictionary containing the sensor data related to the error or unexpected situation.

"""
