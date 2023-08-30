# Functions
# Functions are a convenient way to divide your code into useful blocks, allowing us to order our code, make it more readable, reuse it and save some time. Also functions are a key way to define interfaces so programmers can share their code.
# How do you write functions in Python?

# Syntax
# def functionname( parameters ):
#    "function_docstring"
#    function_suite
#    return [expression]


# Simple Function to add two numbers


def add(a, b):  # type: ignore (ignore type hinting for now)
    return a + b


# Function call

print(add(1, 2))


# Complex Function to add two numbers


def add(a, b, c):
    sum = a + b + c
    return sum


print(add(1, 2, 3))
