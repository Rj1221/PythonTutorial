# In Python Generators are the functions that return an iterable sequence of items one at a time in a special way.

# When an iteration over a set of item starts using the for statement, the generator is run. Once the generator's function code reaches a "yield" statement, the generator yields its execution back to the for loop, returning a new value from the set. The generator function can generate as many values (possibly infinite) as it wants, yielding each one in its turn.

# Syntax

# def generator_function():
#     ...
#     yield value

# Generator function contains one or more yield statement.

# When called, it returns an object (iterator) but does not start execution immediately.

# Here is a simple example of a generator function which returns 7 random integers:

# Example 1
import random


def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1, 15)


for random_number in lottery():
    print("And the next number is... %d!" % (random_number))


# Example 2
# Here is another example where a generator function is used to generate all the even numbers from 0 to the number passed:


def even_numbers(n):
    for i in range(1, n):
        if i % 2 == 0:
            yield i


for number in even_numbers(11):
    print("Even number: ", number)

# Example 3 Generator With **kwargs


def my_gen(**kwargs):
    for key, value in kwargs.items():
        yield key, value


for key, value in my_gen(first="Geeks", mid="for", last="Geeks"):
    print(key, value)

# Multiple Yield Statements
# A generator function can also have multiple yield statements.

# Example 4


def generator():
    yield 1
    yield 2
    yield 3


for value in generator():
    print(value)


# Output:
# 1
# 2
# 3
