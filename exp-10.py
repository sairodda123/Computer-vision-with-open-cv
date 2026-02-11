import cv2
import numpy as np

# Read image
img = cv2.imread(
    r"C:\Users\sairo\OneDrive\Pictures\Screenshots\Screenshot 2026-02-09 140510.png"
)

# Check image loaded
if img is None:
    print("Image not found")
    exit()

# Source points (pick 4 matching points from the image)
pts1 = np.float32([
    [100, 100],
    [300, 100],
    [100, 300],
    [300, 300]
])

# Destination points (shifted / transformed points)
pts2 = np.float32([
    [120, 80],
    [320, 90],
    [130, 320],
    [330, 330]
])

# Find Homography matrix
H, status = cv2.findHomography(pts1, pts2)

# Apply homography
h, w = img.shape[:2]
result = cv2.warpPerspective(img, H, (w, h))

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Homography Transformed Image", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
