import math
def add():
    # Takes user input to add two numbers together
    num1 = input("Please input your first number: ")
    num2 = input("Please input your second number: ")
    sum = float(num1) + float(num2)
    # Displays the first two numbers added together to form the sum
    print('The sum of {0} and {1} is {2}'. format(num1, num2, sum))
    add()
add()