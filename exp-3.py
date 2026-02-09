import cv2

# Open webcam (0 = default camera)
cap = cv2.VideoCapture(0)

mode = "normal"  # normal / slow / fast

print("Press:")
print("n - Normal speed")
print("s - Slow motion")
print("f - Fast motion")
print("q - Quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.putText(frame, f"Mode: {mode}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Webcam Video", frame)

    # Speed control
    if mode == "slow":
        key = cv2.waitKey(100)   # more delay → slow motion
    elif mode == "fast":
        key = cv2.waitKey(1)     # less delay → fast motion
    else:
        key = cv2.waitKey(30)    # normal speed

    # Key controls
    if key == ord('s'):
        mode = "slow"
    elif key == ord('f'):
        mode = "fast"
    elif key == ord('n'):
        mode = "normal"
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
