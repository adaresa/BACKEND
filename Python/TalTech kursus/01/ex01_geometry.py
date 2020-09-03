"""Geometry program."""
import math
# Ask user the shape
print("Please insert geometric shape:")
shape = input()
if shape == "triangle":  # If user chooses triangle
    print("Please insert side length in cm:")
    shape_length = input()  # Gets side length from user
    area = (math.sqrt(3) / 4) * (float(shape_length)**2)  # calc area
elif shape == "circle":  # If user chooses circle
    print("Please insert radius in cm:")
    shape_length = input()  # Gets ring radius from user
    area = math.pi * float(shape_length) * float(shape_length)  # calc area
elif shape == "square":  # If user chooses square
    print("Please insert side length in cm:")
    shape_length = input()  # Gets side length from user
    area = float(shape_length)**2  # calc area
else:  # If user inputs incorrect shape
    print("Shape is not supported.")
# Rounds the area and prints it to the user
area = round(area, 2)
print(f"The area is {area} cm^2")