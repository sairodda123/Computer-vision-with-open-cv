import cv2
import numpy as np

# Read video using given path
cap = cv2.VideoCapture(
    r"C:\Users\sairo\OneDrive\Pictures\WhatsApp Video 2026-02-06 at 13.00.51.mp4"
)

# Source points (change according to your video)
pts1 = np.float32([
    [100, 100],
    [500, 100],
    [100, 400],
    [500, 400]
])

# Destination points
pts2 = np.float32([
    [0, 0],
    [300, 0],
    [0, 300],
    [300, 300]
])

# Perspective matrix
M = cv2.getPerspectiveTransform(pts1, pts2)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Apply perspective transform
    warped = cv2.warpPerspective(frame, M, (300, 300))

    cv2.imshow("Original Video", frame)
    cv2.imshow("Perspective Transformed Video", warped)

    # Press ESC to exit
    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
