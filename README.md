
# Fire Detection System

This repository contains a Python-based fire detection system utilizing OpenCV and image processing techniques. The system processes video footage to identify and classify potential fire regions based on color and size, providing an intensity scale to assess the severity.

## Features

- **Fire Detection by Color**: Identifies potential fire areas based on color ranges, focusing on red, yellow, and purple hues commonly associated with flames.
- **Intensity Scale**: Classifies detected fire regions from levels 1 to 5 based on area size, providing an indication of fire intensity.
- **Real-time Processing**: Processes video footage in real-time, suitable for applications like security cameras or early fire alert systems.
- **Noise Reduction**: Utilizes Gaussian blur and morphological transformations to reduce noise, ensuring accurate fire detection.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- Numpy

Install dependencies via:

```bash
pip install opencv-python-headless numpy imutils
```

## Usage

1. **Setup**: Clone the repository and navigate to the project directory.
2. **Run the Script**: Run the detection script using:

    ```bash
    python fire_detection.py
    ```

3. **Configure Video Source**: The script currently processes a file named `fireabove.mp4` located in the `directory/` folder. Adjust this line if using a different video or webcam (e.g., replace `"directory/fireabove.mp4"` with `0` to use your primary webcam).

## Code Overview

- **Adjust Brightness and Contrast**: The script modifies contrast and brightness for enhanced fire detection in various lighting conditions.
- **Color Filtering**: Defines HSV color ranges for red, purple, and yellow to identify flame colors and avoid overlaps with other hues.
- **Contours and Intensity Assessment**: Detects contours and calculates areas for each contour, classifying fire size on a scale of 1-5:
  - Level 1: Small (area < 2000 pixels)
  - Level 2: Medium-small (2000 ≤ area < 7500 pixels)
  - Level 3: Medium (7500 ≤ area < 14000 pixels)
  - Level 4: Medium-large (14000 ≤ area < 24000 pixels)
  - Level 5: Large (area ≥ 24000 pixels)

## Example

Run the script to display a real-time feed with detected fire regions marked by bounding rectangles and fire intensity levels.

Press `q` to quit the program.
