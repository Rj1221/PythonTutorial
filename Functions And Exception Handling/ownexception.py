# In Python We Can Create Our Own Exception Class
#
# Syntax
# class MyException(Exception):
#     pass
#
# # Example 1: Creating a Custom Exception
class MyException(Exception):
    pass


try:
    raise MyException("An exception doesn't always prove the rule!")
except MyException as e:
    print(e)

# Example 2: Creating a Custom Exception with a Real Example


class CoffeeTooHotException(Exception):
    pass


def coffee_drink(coffee_temperature):
    if coffee_temperature > 75:
        raise CoffeeTooHotException("Coffee is too hot!")
    else:
        print("Coffee is ready to drink!")


coffee_drink(60)

# Example 3: For division by zero we can use ZeroDivisionError


class ZeroDivisionError(Exception):
    pass


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("You cannot divide by zero!")
    except TypeError:
        print("You can divide only numbers!")


divide(1, 0)
