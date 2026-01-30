#   - `add(a, b)`: Returns the sum of two numbers.
#   - `subtract(a, b)`: Returns the difference between two numbers.
#   - `multiply(a, b)`: Returns  multiply between two numbers.
#   -  `division(a, b)`: Returns  division between two numbers.
#         - handel **ZeroDivisionError**


def add(a,b):
    return(a+b)

def subtract(a,b):
    return(a-b)

def multiply(a,b):
    return(a*b)

def division(a,b):
    try:
        return(a/b)
    except ZeroDivisionError:
        print("division by zero")