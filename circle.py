import math

def area(r):
    if r < 0:
        raise ValueError("The radius cannot be negative.")
    return math.pi * r * r

def perimeter(r):
    if r < 0:
        raise ValueError("The radius cannot be negative.")
    
    return 2 * math.pi * r
