import math

def calculate_factorial():
    n = int(input("Enter a number: "))
    print(f"Factorial: {math.factorial(n)}")

def solve_compound_interest():
    p = float(input("Enter principal amount: "))
    r = float(input("Enter rate of interest (in %): "))
    t = float(input("Enter time (in years): "))
    ci = p * (pow((1 + r / 100), t))
    print(f"Compound Interest: {round(ci, 2)}")

def trig_calculations():
    angle = float(input("Enter angle in degrees: "))
    rad = math.radians(angle)
    print(f"Sine: {round(math.sin(rad), 4)}")
    print(f"Cosine: {round(math.cos(rad), 4)}")

def area_geometric():
    r = float(input("Enter radius of circle: "))
    print(f"Area: {round(math.pi * r**2, 2)}")