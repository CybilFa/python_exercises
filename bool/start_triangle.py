def is_valid_triangle(a, b, c):
    """Check if sides can form a triangle"""
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b >= c and a + c >= b and b + c >= a

def equilateral(sides):
    a, b, c = sides
    if not is_valid_triangle(a, b, c):
        return False
    return a == b == c

def isosceles(sides):
    a, b, c = sides
    if not is_valid_triangle(a, b, c):
        return False
    return a == b or b == c or a == c

def scalene(sides):
    a, b, c = sides
    if not is_valid_triangle(a, b, c):
        return False
    return a != b and b != c and a != c
print(isosceles([1, 1, 3]))   
print(equilateral([2, 2, 2])) 
print(scalene([3, 4, 5]))     
print(isosceles([3, 3, 4]))   


