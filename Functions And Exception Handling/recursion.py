# Recursion Means a function calling itself

# Factorial of a number


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(5))


# Fibonacci Series
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))


# Sum of digits
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)


print(sum_of_digits(12345))
