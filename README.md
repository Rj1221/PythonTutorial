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
