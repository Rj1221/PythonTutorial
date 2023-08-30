# Keyword Arguments
# Difference between positional and keyword arguments is that keyword arguments are identified by the parameter name. meaning that you can use the parameter name and the value to pass the argument.

# Keyword Arguments Syntax
# def functionname(parameter1=value1, parameter2=value2, parameter3=value3):
#    "function_docstring"
#    function_suite
#    return [expression]


# Example
# Keyword Arguments
#  Divide Function
def divide(dividend, divisor):
    return dividend / divisor


num1 = int(input("Enter dividend: "))
num2 = int(input("Enter divisor: "))

print(divide(divisor=num2, dividend=num1))
# Output
# Enter dividend: 10
# Enter divisor: 2
