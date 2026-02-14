import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(
    r"C:\Users\sairo\OneDrive\Pictures\Screenshots\Screenshot 2026-02-05 102230.png",
    cv2.IMREAD_GRAYSCALE
)

if img is None:
    print("Error: Image not found")
    exit()

noisy = img.copy()
p = 0.02
rnd = np.random.rand(*img.shape)

noisy[rnd < p/2] = 0
noisy[rnd > 1 - p/2] = 255

gaussian = cv2.GaussianBlur(noisy, (5, 5), 1.0)
median = cv2.medianBlur(noisy, 5)

titles = ["Original", "Noisy", "Gaussian", "Median"]
images = [img, noisy, gaussian, median]

plt.figure(figsize=(10, 6))
for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i], cmap="gray")
    plt.title(titles[i])
    plt.axis("off")

plt.tight_layout()
plt.show()
