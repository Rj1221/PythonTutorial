# PythonTutorial

Python Tutorials For Beginners

![Python Logo](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)

Welcome to the Python Repository! This repository serves as a comprehensive guide to learning Python programming language, covering various topics and concepts with examples and explanations.

## Table of Contents

1. [What is Python](#what-is-python)
2. [Features of Python](#features-of-python)
3. [What is Python Used For](#what-is-python-used-for)
4. [Modules in Python](#modules-in-python)
5. [Types of Modules](#types-of-modules)
   - Built-in Modules
   - External Modules
6. [Our First Program](#our-first-program)
7. [Comments, Escape Sequences, and Print Statement](#comments-escape-sequences-and-print-statement)
8. [Variables](#variables)
9. [Data Types](#data-types)
10. [Operators in Python](#operators-in-python)
    - Arithmetic Operators
    - Comparison Operators
    - Logical Operators
    - Assignment Operators
    - Identity Operators
    - Membership Operators
11. [Type Casting](#type-casting)
    - Implicit Type Casting (Coercion)
    - Explicit Type Casting (Conversion)
12. [Taking Input at Runtime](#taking-input-at-runtime)
13. [Strings and Its Methods](#strings-and-its-methods)
14. [Conditional Statements](#conditional-statements)
15. [Match Case Statements](#match-case-statements)
16. [Looping Statements](#looping-statements)
    - For Loop
    - While Loop
17. [Range and Its Parameters](#range-and-its-parameters)
18. [List](#list)
19. [Tuples](#Tuples)

## What is Python

Python is a high-level, interpreted, and general-purpose programming language known for its simplicity and readability. It is widely used in various domains, including web development, data analysis, artificial intelligence, automation, and more.

## Features of Python

- Easy-to-learn syntax
- Interpreted nature (no need for compilation)
- Extensive standard library
- Dynamic typing
- Object-oriented programming support
- Cross-platform compatibility

## What is Python Used For

Python is used for a wide range of applications, including:

- Web development (using frameworks like Django and Flask)
- Data analysis and visualization (using libraries like NumPy, Pandas, and Matplotlib)
- Machine learning and artificial intelligence (using libraries like TensorFlow and PyTorch)
- Automation and scripting
- Game development
- Network programming
- And much more!

## Modules in Python

Modules in Python are files containing Python code that can be reused in other programs. They help in organizing code and promoting code reusability.

## Types of Modules

### Built-in Modules

Python comes with a rich set of built-in modules that are available for immediate use. Some commonly used built-in modules are:

- `math`
- `random`
- `datetime`
- `os`

### External Modules

External modules are created by the Python community and are not part of the standard Python distribution. They can be installed using package managers like `pip`. For example:

- `requests`
- `beautifulsoup4`
- `matplotlib`

## Our First Program

Let's start with the classic "Hello, World!" program, a simple program that displays the text "Hello, World!" on the screen.

```python
print("Hello, World!")
```

## Comments, Escape Sequences, and Print Statement

Python supports single-line and multi-line comments, escape sequences, and the `print` statement for displaying output.

```python
# This is a single-line comment

"""
This is a multi-line comment.
It can span multiple lines.
"""

print("Hello, Python!")
print("Line 1\nLine 2")
```

## Variables

Variables in Python are used to store data of different data types, such as numbers, strings, or objects.

```python
# Integer variable
age = 25

# String variable
name = "John Doe"

# Floating-point variable
price = 10.99
```

## Data Types

Python supports various data types, including:

- Numeric types (int, float, complex)
- Sequence types (str, list, tuple)
- Boolean type (bool)
- Set types (set, frozenset)
- Mapping type (dict)

```python
# Numeric types
age = 25
salary = 35000.50
complex_number = 3 + 5j

# Sequence types
name = "Alice"
numbers = [1, 2, 3, 4]
coordinates = (10, 20)

# Boolean type
is_valid = True

# Set types
fruits = {"apple", "banana", "orange"}
frozen_fruits = frozenset(fruits)

# Mapping type
person = {"name": "Bob", "age": 30}
```

## Operators in Python

Python supports various types of operators to perform operations on variables and values.

### Arithmetic Operators

```python
a = 10
b = 5

print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulo (Remainder)
print(a ** b) # Exponentiation
```

### Comparison Operators

```python
x = 10
y = 20

print(x == y)  # Equal to
print(x != y)  # Not equal to
print(x < y)   # Less than
print(x > y)   # Greater than
print(x <= y)  # Less than or equal to
print(x >= y)  # Greater than or equal to
```

### Logical Operators

```python
p = True
q = False

print(p and q)  # Logical AND
print(p or q)   # Logical OR
print(not p)    # Logical NOT
```

### Assignment Operators

```python
a = 10
b = 5

a += b  # Equivalent to a = a + b
a -= b  # Equivalent to a = a - b
a *= b  # Equivalent to a = a * b
a /= b  # Equivalent to a = a / b
a %= b  # Equivalent to a = a % b
```

### Identity Operators

```python
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)  # False (x and y are different objects)
print(x is z)  # True (x and z refer to the same object)
print(x is not y)  # True (x and y are different objects)
```

### Membership Operators

```python
fruits = ["apple", "banana", "orange"]

print("apple" in fruits)    # True (apple is in the list)
print("grape" not in fruits)  # True (grape is not in the list)
```

## Type Casting

Type casting allows converting one data type to another.

### Implicit Type Casting (Coercion)

```python
x = 10
y = 5.5

sum = x + y  # Python automatically converts 'x' to float before addition
print(sum)

   # Output: 15.5
```

### Explicit Type Casting (Conversion)

```python
x = "10"
y = 5

sum = int(x) + y  # Convert 'x' to int before addition
print(sum)       # Output: 15
```

## Taking Input at Runtime

You can take user input at runtime using the `input()` function.

```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

## Strings and Its Methods

Strings are sequences of characters in Python. They have various built-in methods for manipulation.

```python
text = "Hello, Python!"

# Length of the string
print(len(text))  # Output: 14

# Convert to uppercase
print(text.upper())  # Output: HELLO, PYTHON!

# Convert to lowercase
print(text.lower())  # Output: hello, python!

# Count occurrences of a substring
print(text.count("o"))  # Output: 2

# Replace a substring
print(text.replace("Python", "World"))  # Output: Hello, World!

# Check if the string starts with a specific prefix
print(text.startswith("Hello"))  # Output: True

# Check if the string ends with a specific suffix
print(text.endswith("Python!"))  # Output: True

# Split the string into a list
print(text.split(","))  # Output: ['Hello', ' Python!']
```

## Conditional Statements

Conditional statements allow executing different code blocks based on certain conditions.

```python
x = 10

if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
```

## Match Case Statements

Match case (available in Python 3.10 and above) provides a more concise way to handle multiple conditions.

```python
fruit = "apple"

match fruit:
    case "apple":
        print("It's an apple.")
    case "banana":
        print("It's a banana.")
    case "orange":
        print("It's an orange.")
    case _:
        print("Unknown fruit.")
```

## Looping Statements

Looping statements allow executing a block of code repeatedly.

### For Loop

```python
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)
```

### While Loop

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

## Range and Its Parameters

`range()` is a built-in function used to generate sequences of numbers.

```python
# Generate numbers from 0 to 9 (excluding 10)
for num in range(10):
    print(num)

# Generate numbers from 5 to 9 (excluding 10)
for num in range(5, 10):
    print(num)

# Generate numbers from 1 to 10 with a step of 2
for num in range(1, 11, 2):
    print(num)
```

## List

List are Mutable and Ordered Collection of items and can be changed or modified after its creation.
List allows duplicate members.
List is a collection which is ordered and changeable. Allows duplicate members.
List is a collection which is ordered and changeable. Allows duplicate members.

## Working with Lists in Python

Lists are mutable data structures in Python, meaning their elements can be changed after creation. Here's how you can perform various operations with lists:

## Assigning Lists

```python
# Lists can be modified, unlike tuples.
l_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(l_list)                 # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(type(l_list))           # Output: <class 'list'>
```

## Accessing List Elements

```python
print(l_list[0])              # Output: 1
print(l_list[1])              # Output: 2
print(l_list[-1])             # Output: 10 (Negative Indexing)
print(l_list[-2])             # Output: 9  (Negative Indexing)
print(l_list[2:5])            # Output: [3, 4, 5] (Range of Indexes)
print(l_list[:5])             # Output: [1, 2, 3, 4, 5] (Range of Indexes)
```

## Loop Through a List

```python
# Loop through a list
for x in l_list:
    print(x, end=",")         # Output: 1,2,3,4,5,6,7,8,9,10,
print()                       # To move to the next line
```

## Modify List Items

```python
# Modify list items directly
l_list[0] = 11
print("Modified list:", l_list)   # Output: Modified list: [11, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

## Check if Item Exists in List

```python
# Check if Item Exists
if 1 in l_list:
    print("Yes, '1' is in the list")  # Output: Yes, '1' is in the list
else:
    print("No, '1' is not in the list")
```

## List Length

```python
print("Length of list:", len(l_list))  # Output: Length of list: 10
```

## Add Items to a List

```python
# Add Items
# You can add items to a list using the append() or extend() method.
l_list.append(11)
print("List after append:", l_list)   # Output: List after append: [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# You can also add multiple items at once using the extend() method.
l_list.extend([12, 13, 14])
print("List after extend:", l_list)   # Output: List after extend: [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
```

## Remove Items from a List

```python
# Remove Items
# You can remove items from a list using the remove() method.
l_list.remove(11)
print("List after remove:", l_list)   # Output: List after remove: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# Alternatively, you can use the pop() method to remove an item at a specific index.
l_list.pop(0)
print("List after pop:", l_list)      # Output: List after pop: [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# To remove all elements, you can use the clear() method.
l_list.clear()
print("List after clear:", l_list)    # Output: List after clear: []
```

## Join Two Lists

```python
l_list1 = [1, 2, 3]
l_list2 = [4, 5, 6]
l_list3 = l_list1 + l_list2
print("Join two lists:", l_list3)    # Output: Join two lists: [1, 2, 3, 4, 5, 6]
```

## List Methods

```python
# count()	Returns the number of times a specified value occurs in a list
l_list4 = [1, 1, 2, 3, 4, 1]
print("Count of 1 in list:", l_list4.count(1))   # Output: Count of 1 in list: 3

# index()	Searches the list for a specified value and returns the index of where it was found
print("Index of 2 in list:", l_list4.index(2))   # Output: Index of 2 in list: 2
```

## Built-in Functions and Operators

```python
# all()	Returns True if all items in an iterable object are true
print("All items in list are true:", all(l_list3))  # Output: All items in list are true: True

# any()	Returns True if any item in an iterable object is true
print("Any item in list is true:", any(l_list3))    # Output: Any item in list is true: True

# len()	Returns the length of an object
print("Length of list:", len(l_list3))             # Output: Length of list: 6

# max()	Returns the largest item in an iterable
print("Max item in list:", max(l_list3))           # Output: Max item in list: 6

# min()	Returns the smallest item in an iterable
print("Min item in list:", min(l_list3))           # Output: Min item in list: 1

# sum()	Returns the sum of all items in an iterable
print("Sum of all items in list:", sum(l_list3))    # Output: Sum of all items in list: 21
```

These are some of the basic operations and methods you can use to work with lists in Python.

## Tuples

Tuples are immutable data structures in Python, which means once they are created, their elements cannot be changed. Let's explore various operations you can perform with tuples:

## Assigning Tuples

```python
# Tuples are immutable, which means you cannot change them once created.
l_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(l_tuple)                # Output: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(type(l_tuple))          # Output: <class 'tuple'>
```

## Accessing Tuple Elements

```python
print(l_tuple[0])             # Output: 1
print(l_tuple[1])             # Output: 2
print(l_tuple[-1])            # Output: 10 (Negative Indexing)
print(l_tuple[-2])            # Output: 9  (Negative Indexing)
print(l_tuple[2:5])           # Output: (3, 4, 5) (Range of Indexes)
print(l_tuple[:5])            # Output: (1, 2, 3, 4, 5) (Range of Indexes)
```

## Loop Through a Tuple

```python
# Loop through a tuple
for x in l_tuple:
    print(x, end=",")         # Output: 1,2,3,4,5,6,7,8,9,10,
print()                       # To move to the next line
```

## Convert Tuple to List and Modify

```python
# Convert the tuple into a list to be able to change it
l_list = list(l_tuple)
l_list[0] = 11
l_tuple = tuple(l_list)
print("Converted to list from tuples:", l_tuple)  # Output: (11, 2, 3, 4, 5, 6, 7, 8, 9, 10)
```

## Check if Item Exists in Tuple

```python
# Check if Item Exists
if 1 in l_tuple:
    print("Yes, '1' is in the tuple")   # Output: Yes, '1' is in the tuple
else:
    print("No, '1' is not in the tuple")
```

## Tuple Length

```python
print("Length of tuple:", len(l_tuple))  # Output: Length of tuple: 10
```

## Join Two Tuples

```python
l_tuple1 = (1, 2, 3)
l_tuple2 = (4, 5, 6)
l_tuple3 = l_tuple1 + l_tuple2
print("Join two tuples:", l_tuple3)     # Output: Join two tuples: (1, 2, 3, 4, 5, 6)
```

## Tuple Methods

```python
# count()	Returns the number of times a specified value occurs in a tuple
print("Count of 1 in tuple:", l_tuple3.count(1))   # Output: Count of 1 in tuple: 1

# index()	Searches the tuple for a specified value and returns the position of where it was found
print("Index of 1 in tuple:", l_tuple3.index(1))   # Output: Index of 1 in tuple: 0
```

## Built-in Functions and Operators

```python
# all()	Returns True if all items in an iterable object are true
print("All items in tuple are true:", all(l_tuple3))  # Output: All items in tuple are true: True

# any()	Returns True if any item in an iterable object is true
print("Any item in tuple is true:", any(l_tuple3))    # Output: Any item in tuple is true: True

# len()	Returns the length of an object
print("Length of tuple:", len(l_tuple3))             # Output: Length of tuple: 6

# max()	Returns the largest item in an iterable
print("Max item in tuple:", max(l_tuple3))           # Output: Max item in tuple: 6

# min()	Returns the smallest item in an iterable
print("Min item in tuple:", min(l_tuple3))           # Output: Min item in tuple: 1

# sum()	Returns the sum of all items in an iterable
print("Sum of all items in tuple:", sum(l_tuple3))    # Output: Sum of all items in tuple: 21
```
