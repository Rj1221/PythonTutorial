# In Python to handle Exceptions we use try and except block
# try block is the block where we write the code which can cause an exception
# except block is the block where we handle the exception
# else block is the block which is executed if there is no exception

# Syntax
# try:
#     # Code which can cause an exception
# except:
#     # Code to handle the exception
# else:
#     # Code which is executed if there is no exception
#
# # Example 1: Handling ZeroDivisionError
try:
    print(1 / 0)
except ZeroDivisionError:
    print("You cannot divide by zero!")
else:
    print("Good job!")

# # Output
# # You cannot divide by zero!


# Example 2: Handling ValueError
try:
    int("Hello")
except ValueError:
    print("You cannot convert a string to an integer!")
else:
    print("Good job!")

# # Output
# # You cannot convert a string to an integer!

# Example 3: Handling Multiple Exceptions
try:
    print(1 / 0)
    int("Hello")
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("You cannot convert a string to an integer!")
else:
    print("Good job!")

# # Output
# # You cannot divide by zero!

# Example 4: Handling Error in a Function


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("You cannot divide by zero!")
    except TypeError:
        print("You can divide only numbers!")
    else:
        print("Good job!")


print(divide(1, 2))
print(divide(1, 0))
print(divide("Hello", "World"))
