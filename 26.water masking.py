import cv2

try:
    img = cv2.imread(r"C:\Users\hp\OneDrive\Pictures\bike.jpg")
    wm = cv2.imread(r"C:\Users\hp\OneDrive\Pictures\Saved Pictures\bike2.jpg")
    
    if img is None or wm is None:
        raise FileNotFoundError("One or more image files not found")

    h_img, w_img = img.shape[:2]
    center_x = int(w_img/2)
    center_y = int(h_img/2)
    
    h_wm, w_wm = wm.shape[:2]
    scale_factor = min(w_img / w_wm, h_img / h_wm)
    new_width = int(w_wm * scale_factor)
    new_height = int(h_wm * scale_factor)
    wm = cv2.resize(wm, (new_width, new_height))

    h_wm, w_wm = wm.shape[:2]
    top_y = center_y - int(h_wm/2)
    left_x = center_x - int(w_wm/2)
    bottom_y = top_y + h_wm
    right_x = left_x + w_wm
    
    roi = img[top_y:bottom_y, left_x:right_x]
    result = cv2.addWeighted(roi, 1, wm, 0.3, 0)
    img[top_y:bottom_y, left_x:right_x] = result
    
    cv2.imshow("Watermarked Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except Exception as e:
    print("An error occurred:", e)
