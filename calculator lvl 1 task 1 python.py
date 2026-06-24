
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

num1 = float(input("enter first number:"))
num2 = float(input("enter second number:"))
operation = input("enter operation (+, -, *, /):")


if operation == "+":
    print("result =", add(num1, num2))
elif operation == "-":
    print("result =", subtract(num1, num2))
elif operation == "*":
    print("result =", multiply(num1, num2))
elif operation == "/":
    if num2 == 0:
        print("cannot divide by zero")
    else:
        print("result =", divide(num1, num2))
else:
    print("invalid operation")