import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\sairo\OneDrive\Pictures\Screenshots\Screenshot 2026-02-09 142044.png")

# Check image loaded
if img is None:
    print("Image not found")
    exit()

(h, w) = img.shape[:2]

# Translation matrix
# Move right by 100 pixels and down by 60 pixels
M = np.float32([[1, 0, 100],
                [0, 1, 60]])

# Apply translation
translated = cv2.warpAffine(img, M, (w, h))

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Translated Image", translated)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\sairo\OneDrive\Pictures\Screenshots\Screenshot 2026-02-09 142044.png")

# Check image loaded
if img is None:
    print("Image not found")
    exit()

(h, w) = img.shape[:2]

# Translation matrix
# Move right by 100 pixels and down by 60 pixels
M = np.float32([[1, 0, 100],
                [0, 1, 60]])

# Apply translation
translated = cv2.warpAffine(img, M, (w, h))

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Translated Image", translated)
cv2.waitKey(0)
cv2.destroyAllWindows()
