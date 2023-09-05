# Decorators are functions that take another function as an argument, add some kind of functionality, and then return another function. All of this without altering the source code of the original function that we passed in.
# Decorators are usually called before the definition of a function you want to decorate.
# Decorators are used to add functionality to a function by wrapping it with another function.
# Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class.
# Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it.

# Syntax:
# def decorator_function(original_function):
#     def wrapper_function():
#         return original_function()
#     return wrapper_function


# Example
def decorator_function(original_function):
    def wrapper_function():
        return original_function()

    return wrapper_function


def display():
    print("display function ran")


decorated_display = decorator_function(display)
decorated_display()

# Real world example
# Decorators are used in web frameworks like Flask and Django for creating web applications.


# Example
def decorator_function(original_function):
    def wrapper_function():
        print("wrapper executed this before {}".format(original_function.__name__))
        return original_function()

    return wrapper_function


@decorator_function
def display():
    print("display function ran")
