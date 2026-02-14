import cv2
import numpy as np

a = cv2.imread(r"C:\Users\hp\OneDrive\Pictures\Saved Pictures\bike.jpeg", cv2.IMREAD_GRAYSCALE)

laplacian1 = np.array([0, 1, 0, 1, -4, 1, 0, 1, 0]).reshape(3, 3)
laplacian2 = np.array([-1, -1, -1, -1, 8, -1, -1, -1, -1]).reshape(3, 3)

a1 = cv2.filter2D(a, -1, laplacian1)
a2 = cv2.filter2D(a1, -1, laplacian2)

a2 = np.uint8(a2)

cv2.imshow("Filtered Image 1", a1)
cv2.imshow("Filtered Image 2", a2)
cv2.waitKey(0)
cv2.destroyAllWindows()
