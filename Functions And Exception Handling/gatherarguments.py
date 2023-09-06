# Gather Positional Arguments with *
# We can use * to gather positional arguments as a tuple. means we do not know how many arguments we will get.


def add(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  # 55
print(add(1, 2, 3, 4))  # 10


# Take a look at another example with fruits


def fruits(*names):  # type: ignore
    print("Fruits I like:")
    for name in names:
        print(name)


print(fruits("Orange", "Apple", "Banana"))
# Output
# Fruits I like:
# Orange
# Apple
# Banana
# None # None is returned because the function doesn't explicitly return a value.

# We can solve None Value By


def fruits(*names):
    print("Fruits I like:")
    for name in names:
        print(name)
    return names


print(fruits("Orange", "Apple", "Banana"))


# Gather Keyword Arguments with **
# Similarly, ** can be used to gather all the keyword arguments as a dictionary. Before we see how that works, let's recall that a dictionary has keys and values: {'key1':'value1', 'key2':'value2', ...}.
# In our example, we will use the keys as the parameter names and the values as the arguments. We can access these arguments like we access any other values in a dictionary.


# Example 1: Gather Keyword Arguments
def kwargs(**kwargs):  # type: ignore
    print(kwargs)


kwargs(name="Bruce", age=24, country="NZ")
# Output
# {'name': 'Bruce', 'age': 24, 'country': 'NZ'}

# Example 2: Gather Keyword Arguments
# We can use the **kwargs parameter as a dictionary inside the function body.


def kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")


kwargs(name="Bruce", age=24, country="NZ")
# Output
# name = Bruce
# age = 24
# country = NZ


def evenOdd(*number):
    """
    The function `evenOdd` takes in a variable number of arguments, separates them into even and odd
    numbers, and returns two lists containing the even and odd numbers respectively.
    :return: The function `evenOdd` returns two lists: `even_list` and `odd_list`.
    """
    even_list = []
    odd_list = []
    for i in number:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return even_list, odd_list


even, odd = evenOdd(5, 4, 1, 3, 9, 6, 7, 12, 18, 22, 34, 54, 98)
sorted_even = sorted(even)
sorted_odd = sorted(odd)
print(sorted_even)
print(sorted_odd)
