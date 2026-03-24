import cv2
import numpy as np

# 1. Read image
image = cv2.imread('input.jpg')

# 2. Resize (optional)
image = cv2.resize(image, (600, 600))

# 3. Smooth image (reduce noise, keep edges)
smooth = cv2.bilateralFilter(image, 9, 100, 100)

# 4. Convert to grayscale
gray = cv2.cvtColor(smooth, cv2.COLOR_BGR2GRAY)

# 5. Laplacian edge detection
laplacian = cv2.Laplacian(gray, cv2.CV_8U, ksize=5)

# 6. Normalize edges (avoid harsh white areas)
edges = cv2.normalize(laplacian, None, 0, 255, cv2.NORM_MINMAX)

# 7. Invert edges
edges_inv = cv2.bitwise_not(edges)

# 8. Convert edges to 3-channel
edges_colored = cv2.cvtColor(edges_inv, cv2.COLOR_GRAY2BGR)

# 9. Sharpen image
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])
sharpened = cv2.filter2D(smooth, -1, kernel)

# 10. Color quantization (cartoon effect)
data = np.float32(sharpened).reshape((-1, 3))
K = 8  # number of colors

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)
_, labels, centers = cv2.kmeans(data, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

centers = np.uint8(centers)
quantized = centers[labels.flatten()]
quantized = quantized.reshape(image.shape)

# 11. Blend edges with color (avoid white patches)
cartoon = cv2.multiply(quantized, edges_colored, scale=1/255)

# 12. Convert to HSV for brightness & color enhancement
hsv = cv2.cvtColor(cartoon, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

# 13. Increase saturation and brightness
s = cv2.multiply(s, 1.5)
v = cv2.multiply(v, 1.2)

s = np.clip(s, 0, 255)
v = np.clip(v, 0, 255)

# 14. Merge and convert back to BGR
hsv_final = cv2.merge([h, s.astype(np.uint8), v.astype(np.uint8)])
final = cv2.cvtColor(hsv_final, cv2.COLOR_HSV2BGR)

# 15. Save output
cv2.imwrite('cartoon_output.jpg', final)

# 16. Display images
cv2.imshow('Original Image', image)
cv2.imshow('Cartoon Image', final)

cv2.waitKey(0)
cv2.destroyAllWindows()