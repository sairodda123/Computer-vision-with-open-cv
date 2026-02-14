import cv2

# Video file path
video_path = r"C:\Users\sairo\OneDrive\Pictures\WhatsApp Video 2026-02-06 at 13.00.51.mp4"

# Open video
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Video Playback", frame)

    # -------- CHANGE SPEED HERE --------
    # Normal speed  → delay = 30
    # Slow motion   → delay = 100
    # Fast motion   → delay = 5

    key = cv2.waitKey(100)   # change this value for speed control

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
