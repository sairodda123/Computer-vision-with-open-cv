import cv2
import numpy as np

def recognize_watch(image_path):
    # Load pre-trained Caffe model
    net = cv2.dnn.readNetFromCaffe(cv2.samples.findFile('MobileNetSSD_deploy.prototxt'), 
                                    cv2.samples.findFile('MobileNetSSD_deploy.caffemodel'))

    # Load input image
    try:
        image = cv2.imread(image_path)
        if image is None:
            print("Error: Unable to load image from path:", image_path)
            return
    except Exception as e:
        print("Error loading image:", e)
        return

    image_height, image_width, _ = image.shape

    # Prepare input image for object detection
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)

    # Set input to the network
    net.setInput(blob)

    # Run forward pass to get output of the output layers
    detections = net.forward()

    # Loop over the detections
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:  # Filter out weak detections
            class_id = int(detections[0, 0, i, 1])
            if class_id == 8:  # 8 corresponds to the class ID of 'watch' in Caffe model
                # Draw bounding box around the detected watch
                box = detections[0, 0, i, 3:7] * np.array([image_width, image_height, image_width, image_height])
                (startX, startY, endX, endY) = box.astype("int")
                cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
                cv2.putText(image, 'Watch', (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the image with bounding box
    cv2.imshow("Watch Recognition", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Path to the input image
image_path = r"C:\Users\hp\OneDrive\Pictures\Saved Pictures\watch.jpeg"

# Call the function to recognize watch in the image
recognize_watch(image_path)
