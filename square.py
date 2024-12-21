def area(a):
    if a < 0:
        raise ValueError("The side of the square cannot be negative.")
    return a * a


def perimeter(a):
    if a < 0:
        raise ValueError("The side of the square cannot be negative.")
    return 4 * a
