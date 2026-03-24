# Cartoon Vision

A computer vision project that converts real-world images into cartoon-style representations using OpenCV.

---

## Description

Cartoon Vision is an image processing program designed to transform standard photographs into stylized cartoon images. The system applies a sequence of computer vision techniques to simplify visual details while preserving essential structures such as edges and object boundaries.

The transformation process focuses on reducing noise, enhancing edges, limiting color variations, and improving visual clarity. As a result, the output image achieves a cartoon-like appearance characterized by bold outlines and smooth, vivid color regions.

---

## Features

- Cartoon-style image transformation  
- Edge detection using Laplacian operator  
- Noise reduction using bilateral filtering  
- Color simplification through K-means clustering  
- Image sharpening for enhanced clarity  
- Brightness and saturation adjustment using HSV color space  

---

## Requirements

opencv-python  
numpy  

Install dependencies using:

pip install opencv-python numpy

---

## How to Run

1. Place your input image in the project directory  
2. Rename the file as:

input.jpg  

3. Execute the program:

python cartoon.py  

4. The processed image will be saved as:

cartoon_output.jpg  

---

## Input and Output

### Input Image
![Input Image](input.jpg)

### Output Image
![Output Image](cartoon_output.jpg)

---

## Project Structure

Cartoon-Vision/  
│── README.md 
│── cartoon.py  
│── input.jpg  
│── cartoon_output.jpg  
 
---

## Methodology

The program follows a multi-stage image processing pipeline:

1. The input image is smoothed using bilateral filtering to reduce noise while preserving important edges.  
2. The image is converted to grayscale for edge detection.  
3. The Laplacian operator is applied to extract prominent edges.  
4. A sharpening filter is used to enhance structural details.  
5. K-means clustering is applied to reduce the number of colors, producing flat color regions.  
6. Edge information is combined with the quantized image to form a cartoon effect.  
7. The final image is enhanced in the HSV color space to improve brightness and color intensity.  

---

## Notes

- The number of clusters (K) in K-means affects the level of color simplification.  
- Lower values of K produce stronger cartoon effects, while higher values retain more detail.  
- High-resolution images generally produce better results.  
