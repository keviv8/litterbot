# Litterbot

Litterbot is an AI-driven robot designed to identify, collect, and manage waste in various environments. It utilizes a combination of real-time video processing, object detection, and autonomous navigation to efficiently clean up litter.

## Architecture Overview

Litterbot's system is divided into several key components:

- **Vision System**: Handles real-time video acquisition, object detection, depth estimation, and optional semantic segmentation.
- **Planning System**: Manages path planning and grasp planning to navigate and interact with the environment.
- **Control System**: Controls the bot's movements and manipulator for picking up litter.
- **Network System**: Manages communication with the central AI system, TerraSync, and handles MQTT messaging.
- **Power Management System**: Monitors battery life and power consumption.
- **User Interface (Optional)**: Provides visualization of the bot's operations and detections.

## Directory Structure

- `control/`: Motor control and other bot control-related scripts.
- `main.py`: The main entry point for the Litterbot's operations.
- `network/`: Communication and network-related modules.
- `planning/`: Path and grasp planning algorithms.
- `sandbox/`: Testing and experimental scripts.
- `temp/`: Temporary files and scripts for environment setup.
- `vision/`: Modules for video acquisition, object detection, and other vision-related tasks.
- `visualization/`: Visualization tools for monitoring the bot's operations.

## Getting Started

To get started with Litterbot:

1. Clone the repository to your local machine.
2. Navigate to the project directory and install the required dependencies.
3. Run `main.py` to start the bot's operation simulation.

Please refer to the individual scripts within each directory for detailed usage and testing instructions.

## Contribution

We welcome contributions to Litterbot! If you have suggestions or improvements, please open an issue or submit a pull request.

## License

Litterbot is open-source and available under the [MIT License](https://github.com/keviv8/litterbot/blob/main/LICENSE).
