"""12. Write a Python module named calculator.py containing functions for addition, subtraction,
multiplication, and division."""

def addition(*lst):
    summ = 0
    for i in lst:
        summ += i
    print(f"Summation: {summ}")
    
def subtraction(x, y):
    print(f"Subtraction: {x - y}")
    
def multiplication(*lst):
    prod = 1
    for i in lst:
        prod *= i
    print(f"Multiplication: {prod}")

def division(x, y):
    print(f"Quotient: {x / y}")
    
def int_division(x, y):
    print(f"Quotient: {int(x / y)}, Remainder: {x % y}")