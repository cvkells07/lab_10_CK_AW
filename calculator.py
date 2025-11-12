import math
def square_root(a): 
    if a < 0:
        raise ValueError("square root cannont be for a num less than zero")
    return math.sqrt(a)

def hypotenuse(a, b): 
    return math.hypot(a, b)

def add(a, b): 
    return a + b

def subtract(a, b): 
    return a - b

def mul(a, b): 
    return a * b

def div(a, b): 
    if a == 0:
        raise ZeroDivisionError("division by zero")
    return b/a

def logarithm(a, b):
    if a <= 0:
        raise ValueError("logarithm undefined for non-positive a")
    if b <= 0 or b == 1:
        raise ValueError("base must be positive and not equal to 1")
    return math.log(a, b)

def exp(a, b): 
    return a**b