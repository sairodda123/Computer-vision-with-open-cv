import cv2

img = cv2.imread(r"C:\Users\sairo\OneDrive\Pictures\image.jpg")
(h, w) = img.shape[:2]
center = (w//2, h//2)

# Clockwise (−45 degrees)
M1 = cv2.getRotationMatrix2D(center, -45, 1)
clockwise = cv2.warpAffine(img, M1, (w, h))

# Counter-clockwise (+45 degrees)
M2 = cv2.getRotationMatrix2D(center, 45, 1)
counter = cv2.warpAffine(img, M2, (w, h))

cv2.imshow("Clockwise", clockwise)
cv2.imshow("Counter Clockwise", counter)
cv2.waitKey(0)
cv2.destroyAllWindows()
