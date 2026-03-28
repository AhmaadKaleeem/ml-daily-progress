# Your robot arm has a camera. The camera sees pixels. You need to convert pixel coordinates to real-world inches so the robot knows where to move.
import numpy as np
import pandas as pd

# Given Dataset Values
pixels = [100, 200, 300, 400, 500]  # Camera Pixel coordinates - X
pixel_to_inches = [2.0,4.0,6.0,8.0,10.0]  # Corresponding real-world inches - Y
sum_of_xy = 0.0
sum_x2 = 0.0
# Step 1: Calculate the slope (m) and intercept (b) for the linear regression line
n = len(pixels)
for x,y in zip(pixels,pixel_to_inches):
    sum_x2 += x * x
    sum_of_xy += (x*y) 

mean_pixels = sum(pixels) / n
mean_pixels_to_in = sum(pixel_to_inches) / n
# slope m
slope = (sum_of_xy - (n * (mean_pixels)*(mean_pixels_to_in))) / (sum_x2 -  (n * mean_pixels* mean_pixels))
# finding b intercept = mean of y - slope(m) * mean value of x
intercept = mean_pixels_to_in - slope * mean_pixels

# regression = mx + c (m slope , c interceprt , x value to be predicted)
value_x = float(input("Enter Pixels : "))
predicted_value = (slope * value_x ) + intercept

print(f"Predicted Value for Pixels {value_x} is {predicted_value} Inches")



