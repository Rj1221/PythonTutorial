# Default Arguments
# Default arguments are arguments that are given a default value in the function definition.


def add(a, b=10):
    return a + b


print(add(5))
print(add(5, 15))
# Output
# 15
# 20

# Example 2: Default Arguments


def greet(name, msg="Good morning!"):
    """
    This function greets to
    the person with the
    provided message.

    If message is not provided,
    it defaults to "Good
    morning!"
    """

    print("Hello", name + ", " + msg)


greet("Kate")
greet("Bruce", "How do you do?")

# Example 3: Default arguments


def multiply(a=12, b=2):
    return a * b


print(multiply(5, 4))  # 20
print(multiply(5))  # 10
print(multiply())  # 24
