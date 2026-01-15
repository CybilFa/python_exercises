# Newton's method
#xn+1​=0.5(xn​+S/xn​)
# import math

# def sqrt(x):
#     return math.sqrt(x)


def sqrt(S, tolerance=1e-10):
    if S < 0 :
        raise ValueError("Cannot compute square root of negative number")
    x = S
    while True:
        next_x = 0.5 * (x + S / x)
        if abs(x - next_x) < tolerance:
            return next_x
        x = next_x

print(sqrt(25))