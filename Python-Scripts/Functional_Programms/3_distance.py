'''3. Write a program Distance.java that takes two integer command-line arguments x
and y and prints the Euclidean distance from the point (x, y) to the origin (0, 0). The
formulae to calculate distance = sqrt(x*x + y*y). Use Math.power function'''

import math

x = int(input("Enter x-coordinate: "))
y = int(input("Enter y-coordinate: "))

distance = math.sqrt(math.pow(x, 2) + math.pow(y, 2))

print(f"The Euclidean distance from ({x}, {y}) to (0,0) is: {distance}")