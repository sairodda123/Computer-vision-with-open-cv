import cv2

vehicle_cascade = cv2.CascadeClassifier('vehicle_cascade.xml')

frame = cv2.imread(r"C:\Users\hp\Videos\praises\video 1.mp4")

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

vehicles = vehicle_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

for (x, y, w, h) in vehicles:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('Vehicle Detection', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
