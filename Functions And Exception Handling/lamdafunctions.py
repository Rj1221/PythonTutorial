# Anonymous Functions in Python are the functions which are defined without a name. also known as lambda functions.

# Syntax of Lambda Function in python
# lambda arguments: expression

# Example of Lambda Function in python
# Program to show the use of lambda functions

double = lambda x: x * 2
print(double(5))  # Output: 10

# Create a lamda function to add two numbers
add = lambda x, y: x + y
print(add(5, 6))

# Real Life Example of Lambda Function in python
# Program to filter out the list which contains odd numbers

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x % 2 == 0), my_list))
print(new_list)  # Output: [4, 6, 8, 12]


lambda x: x * 2

# is equivalent to
# def double(x):
#     return x * 2
