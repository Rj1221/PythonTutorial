# Docstrings
# Docstrings are used to describe what your function does, such as the computations it performs or its return value.

# Docstrings are placed in the immediate line after the function header.

# Docstrings are surrounded by triple quotes.

# Docstrings can be single line or multi-line.

# Docstrings are optional, but they are a good programming practice, so you should use them.

# Docstrings are accessible through the __doc__ attribute of the function.


# Example 1: Docstrings
def add(a, b):
    """This function adds two numbers."""  # Docstring
    return a + b


print(add.__doc__)  # This will Access Docstring of add function
# Output: This function adds two numbers.
print(add(5, 4))  # 9
