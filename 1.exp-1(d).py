import cv2
import numpy as np

# Read the image in grayscale
img = cv2.imread(r"C:\Users\sairo\OneDrive\Pictures\Screenshots\Screenshot 2026-02-06 124254.png", 0)

# Create a 5x5 kernel
kernel = np.ones((5, 5), np.uint8)

# Apply dilation
dilated = cv2.dilate(img, kernel, iterations=1)

# Show images
cv2.imshow("Original Image", img)
cv2.imshow("Dilated Image", dilated)

cv2.waitKey(0)
cv2.destroyAllWindows()
