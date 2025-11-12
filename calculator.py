import math
def add(a, b): 
    return a + b

def sub(a, b): 
    return a - b

def mul(a, b): 
    return a * b

def div(a, b): 
    if a == 0:
        raise ZeroDivisionError("division by zero")
    return b/a

def log(a, b):
    if a <= 0:
        raise ValueError("logarithm undefined for non-positive a")
    if b <= 0 or b == 1:
        raise ValueError("base must be positive and not equal to 1")
    return math.log(a, b)

def exp(a, b): 
    return a**b