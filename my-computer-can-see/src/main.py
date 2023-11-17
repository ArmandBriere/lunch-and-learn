import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


# Load duck
img = cv.imread("duck.jpg")

# 2D Convolution - 15x15 filter
kernel = np.ones((15, 15), np.float32) / 250
blur = cv.filter2D(img, -1, kernel)
cv.imwrite("duck-2dconv.jpg", blur)

# Default blur - 15x15 filter
blur = cv.blur(img, (15, 15))
cv.imwrite("duck-blur.jpg", blur)

# Gaussian
blur = cv.GaussianBlur(img, (15, 15), 0)
cv.imwrite("duck-gaussian.jpg", blur)


# Load froge
img = cv.imread("froge.jpg", cv.IMREAD_GRAYSCALE)

# Canny - img, Threshold1,Threshold2
edges = cv.Canny(img, 50, 200)

cv.imwrite("froge-canny.jpg", edges)


# Apply CLAHE on grayscale
img = cv.imread("mountain.jpg", cv.IMREAD_GRAYSCALE)
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(img)

cv.imwrite("mountain-clahe-grayscale.jpg", cl1)


# Apply CLAHE on color
img = cv.imread("mountain.jpg", cv.IMREAD_ANYCOLOR)
img = cv.cvtColor(img, cv.COLOR_RGB2Lab)

clahe = cv.createCLAHE(clipLimit=10, tileGridSize=(8, 8))
img[:, :, 0] = clahe.apply(img[:, :, 0])
img = cv.cvtColor(img, cv.COLOR_Lab2RGB)

cv.imwrite("mountain-clahe-rgb.jpg", img)
