from imutils import paths
import cv2
import numpy as np

video = cv2.VideoCapture("directory/fireabove.mp4")  # Use webcam by setting index like 0,1.

while True:
    (grabbed, frame) = video.read()
    
    # Resize frame for easier processing
    frame = cv2.resize(frame, (960, 540))
    other = frame.copy()
    
    # Adjust contrast and brightness for fire detection
    frame = cv2.convertScaleAbs(frame, alpha=1.4, beta=-100)

    # Blur and convert to HSV
    blur = cv2.GaussianBlur(frame, (21, 21), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    # Define tighter HSV ranges for red, purple, and yellow colors, avoiding green overlap
    lower_red = np.array([0, 100, 100], dtype="uint8")
    upper_red = np.array([10, 255, 255], dtype="uint8")

    lower_purple = np.array([135, 70, 100], dtype="uint8")
    upper_purple = np.array([155, 255, 255], dtype="uint8")

    lower_yellow = np.array([15, 150, 200], dtype="uint8")
    upper_yellow = np.array([35, 255, 255], dtype="uint8")

    # Create masks for each color
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_purple = cv2.inRange(hsv, lower_purple, upper_purple)
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Combine masks for fire detection
    mask = cv2.bitwise_or(mask_red, mask_purple)
    mask = cv2.bitwise_or(mask, mask_yellow)

    # Apply morphological transformations for noise reduction
    mask = cv2.dilate(mask, None, iterations=2)
    mask = cv2.erode(mask, None, iterations=1)

    # Find contours in the combined mask
    contours_fire, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    output = cv2.bitwise_and(frame, frame, mask=mask)
    no_fire = cv2.countNonZero(mask)

    # Process each contour
    for cnt in contours_fire:
        x, y, w, h = cv2.boundingRect(cnt)
        contour_area = cv2.contourArea(cnt)

        if contour_area > 700:
            # Draw bounding rectangle and label intensity based on size
            rectangle = cv2.rectangle(other, (x, y), (x + w, y + h), (255, 255, 0), 2)
            area = w * h
            if area < 2000:
                cv2.putText(other, '1', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            elif 2000 <= area < 7500:
                cv2.putText(other, '2', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            elif 7500 <= area < 14000:
                cv2.putText(other, '3', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            elif 14000 <= area < 24000:
                cv2.putText(other, '4', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            else:
                cv2.putText(other, '5', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Display the processed frames
    cv2.imshow('Original with Detections', other)
    cv2.imshow("Adjusted Frame", frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# Cleanup
cv2.destroyAllWindows()
video.release()
