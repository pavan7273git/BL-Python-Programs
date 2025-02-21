'''Write a program Quadratic.java to find the roots of the equation a*x*x + b*x + c.
Since the equation is x*x, hence there are 2 roots. The 2 roots of the equation
can be found using a formula (Note: Take a, b and c as input values)
delta = b*b - 4*a*c
Root 1 of x = (-b + sqrt(delta))/(2*a)
Root 2 of x = (-b - sqrt(delta))/(2*a)'''

import math


a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))


delta = math.pow(b, 2) - 4 * a * c


if delta > 0:
    root1 = (-b + math.sqrt(delta)) / (2 * a)
    root2 = (-b - math.sqrt(delta)) / (2 * a)
    print("Roots are real and distinct.")
    print("Root 1:", root1)
    print("Root 2:", root2)
elif delta == 0:
    root = -b / (2 * a)
    print("Roots are real and equal.")
    print("Root:", root)
else:
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(-delta) / (2 * a)
    print("Roots are complex and imaginary.")
    print(f"Root 1: {real_part} + {imaginary_part}i")
    print(f"Root 2: {real_part} - {imaginary_part}i")