import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\sairo\OneDrive\Pictures\Screenshots\Screenshot 2025-06-04 123148.png")

# Check image
if img is None:
    print("Image not found")
    exit()

(h, w) = img.shape[:2]

# Translation matrix
# Move right by 120 pixels and down by 80 pixels
M = np.float32([[1, 0, 120],
                [0, 1, 80]])

# Apply translation
translated = cv2.warpAffine(img, M, (w, h))

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Translated Image", translated)
cv2.waitKey(0)
cv2.destroyAllWindows()
