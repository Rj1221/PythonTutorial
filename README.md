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
    - Implicit Type Casting (Conversion)
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
19. [Tuples](#tuples)
20. [Break and Continue](#break-and-continue)
21. [Set and FrozenSet](#set-and-frozenset)
22. [Dictionary](#dictionary)
23. [Functions and Exception Handling](#functions-and-exception-handling)
    - Functions
    - Positional Arguments
    - Keyword Arguments
    - Default Arguments
    - Gather Positional Arguments \*
    - Gather Keyword Arguments \*\*

## What is Python

Python is a high-level, interpreted, and general-purpose programming language known for its simplicity and readability. It is widely used in various domains, including web development, data analysis, artificial intelligence, automation, and more.

**[⬆ Back to Top](#table-of-contents)**

## Features of Python

- Easy-to-learn syntax
- Interpreted nature (no need for compilation)
- Extensive standard library
- Dynamic typing
- Object-oriented programming support
- Cross-platform compatibility
- Open-source community development

**[⬆ Back to Top](#table-of-contents)**

## What is Python Used For

Python is used for a wide range of applications, including:

- Web development (using frameworks like Django and Flask)
- Data analysis and visualization (using libraries like NumPy, Pandas, and Matplotlib)
- Machine learning and artificial intelligence (using libraries like TensorFlow and PyTorch)
- Automation and scripting
- Game development
- Network programming
- And much more!

**[⬆ Back to Top](#table-of-contents)**

## Modules in Python

Modules in Python are files containing Python code that can be reused in other programs. They help in organizing code and promoting code reusability.

**[⬆ Back to Top](#table-of-contents)**

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

**[⬆ Back to Top](#table-of-contents)**

## Our First Program

Let's start with the classic "Hello, World!" program, a simple program that displays the text "Hello, World!" on the screen.

```python
print("Hello, World!")
```

**[⬆ Back to Top](#table-of-contents)**

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

**[⬆ Back to Top](#table-of-contents)**

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

**[⬆ Back to Top](#table-of-contents)**

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

**[⬆ Back to Top](#table-of-contents)**

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

**[⬆ Back to Top](#table-of-contents)**

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

**[⬆ Back to Top](#table-of-contents)**

## Taking Input at Runtime

You can take user input at runtime using the `input()` function.

```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

**[⬆ Back to Top](#table-of-contents)**

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

**[⬆ Back to Top](#table-of-contents)**

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

**[⬆ Back to Top](#table-of-contents)**

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

**[⬆ Back to Top](#table-of-contents)**

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

**While Loop with Else**

```python
count = 1

while count <= 5:
    print(count)
    count += 1
else:
    print("Count is greater than 5")
```

**[⬆ Back to Top](#table-of-contents)**

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

**[⬆ Back to Top](#table-of-contents)**

## List

List are Mutable and Ordered Collection of items and can be changed or modified after its creation.
List allows duplicate members.
List is a collection which is ordered and changeable. Allows duplicate members.
List is a collection which is ordered and changeable. Allows duplicate members.
**[⬆ Back to Top](#table-of-contents)**

## Working with Lists in Python

Lists are mutable data structures in Python, meaning their elements can be changed after creation. Here's how you can perform various operations with lists:
**[⬆ Back to Top](#table-of-contents)**

## Assigning Lists

```python
# Lists can be modified, unlike tuples.
l_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(l_list)                 # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(type(l_list))           # Output: <class 'list'>
```

**[⬆ Back to Top](#table-of-contents)**

## Accessing List Elements

```python
print(l_list[0])              # Output: 1
print(l_list[1])              # Output: 2
print(l_list[-1])             # Output: 10 (Negative Indexing)
print(l_list[-2])             # Output: 9  (Negative Indexing)
print(l_list[2:5])            # Output: [3, 4, 5] (Range of Indexes)
print(l_list[:5])             # Output: [1, 2, 3, 4, 5] (Range of Indexes)
```

**[⬆ Back to Top](#table-of-contents)**

## Loop Through a List

```python
# Loop through a list
for x in l_list:
    print(x, end=",")         # Output: 1,2,3,4,5,6,7,8,9,10,
print()                       # To move to the next line
```

**[⬆ Back to Top](#table-of-contents)**

## Modify List Items

```python
# Modify list items directly
l_list[0] = 11
print("Modified list:", l_list)   # Output: Modified list: [11, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

**[⬆ Back to Top](#table-of-contents)**

## Check if Item Exists in List

```python
# Check if Item Exists
if 1 in l_list:
    print("Yes, '1' is in the list")  # Output: Yes, '1' is in the list
else:
    print("No, '1' is not in the list")
```

**[⬆ Back to Top](#table-of-contents)**

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

# Insert Items
# You can insert items at a given index using the insert() method.
l_list.insert(0, 0)
print("List After Insert:",l_list) #Output :List after Insert: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

```

**[⬆ Back to Top](#table-of-contents)**

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

**[⬆ Back to Top](#table-of-contents)**

## Join Two Lists

```python
l_list1 = [1, 2, 3]
l_list2 = [4, 5, 6]
l_list3 = l_list1 + l_list2
print("Join two lists:", l_list3)    # Output: Join two lists: [1, 2, 3, 4, 5, 6]
```

**[⬆ Back to Top](#table-of-contents)**

## List Methods

```python
# count()	Returns the number of times a specified value occurs in a list
l_list4 = [1, 1, 2, 3, 4, 1]
print("Count of 1 in list:", l_list4.count(1))   # Output: Count of 1 in list: 3

# index()	Searches the list for a specified value and returns the index of where it was found
print("Index of 2 in list:", l_list4.index(2))   # Output: Index of 2 in list: 2
```

**[⬆ Back to Top](#table-of-contents)**

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
**[⬆ Back to Top](#table-of-contents)**

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

**[⬆ Back to Top](#table-of-contents)**

## Tuple Methods

```python
# count()	Returns the number of times a specified value occurs in a tuple
print("Count of 1 in tuple:", l_tuple3.count(1))   # Output: Count of 1 in tuple: 1

# index()	Searches the tuple for a specified value and returns the position of where it was found
print("Index of 1 in tuple:", l_tuple3.index(1))   # Output: Index of 1 in tuple: 0
```

**[⬆ Back to Top](#table-of-contents)**

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

**[⬆ Back to Top](#table-of-contents)**

## Break and Continue

**Break**
The Break statement enables a program to skip over a part of the code. A Break statement terminates the very loop it lies within.
**Example:**

```python
for i in range(1, 11):
    print(i, end=" ")
    if i == 5:
        break
    else:
        print("else block")
print("outside for loop")
```

**Example**

```python
num = int(input("Enter a number to print Table: "))
for i in range(1,20):
    if i == 11:
        break
    else:
        print(num,"x",i,"=",num*i)

# Output:
# Enter a number to print Table: 5
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50 It will come out of the loop after 10

```

**[⬆ Back to Top](#table-of-contents)**

# Continue

The continue statement is used to skip the current iteration of the loop and continue with the next iteration.

```python
num=int(input("Enter a number to print Table: "))
for i in range(1, 13):
    if i == 10:
        continue  # skip the current iteration and continue with the next iteration means it will skip 10 and continue with 11
    else:
        print(num,"x",i,"=",num*i)

#Output:
# Enter a number to print Table: 5
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
#Skip 10
# 5 x 11 = 55
# 5 x 12 = 60
# outside for loop

```

## **[⬆ Back to Top](#table-of-contents)**

# Set and FrozenSet

### Set

A `set` is an unordered and unindexed collection of unique elements. It's mutable, meaning you can add or remove items after creation.

#### Creating a Set

```python
# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

# set cannot have duplicates
my_set = {1, 2, 3, 4, 3, 2}
print(my_set)
```

#### Methods and Examples

```python
# initialize my_set
my_set = {1, 3}
print(my_set)  # Output: {1, 3}

# add an element
my_set.add(2)
print(my_set)  # Output: {1, 2, 3}

# add multiple elements
my_set.update([2, 3, 4])
print(my_set)  # Output: {1, 2, 3, 4}

# add list and set
my_set.update([4, 5], {1, 6, 8})
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 8}

# copy my_set
my_set2 = my_set.copy()
print(my_set2)  # Output: {1, 2, 3, 4, 5, 6, 8}

# pop an element
print(my_set2.pop())  # Output: 1

# remove an element
my_set2.remove(8)
print(my_set2)  # Output: {2, 3, 4, 5, 6}

# difference()
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# set1 - set2
print(set1.difference(set2))  # Output: {1, 2, 3}

# intersection()
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# set1 intersection set2
print(set1.intersection(set2))  # Output: {4, 5}

# union()
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# union of two sets
set3 = set1.union(set2)
print(set3)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
```

**[⬆ Back to Top](#table-of-contents)**

### FrozenSet

A `frozenset` is an immutable version of a `set`. It's hashable, can be used as a dictionary key, and can't be changed after creation. It's often used in situations where immutability is required.

#### Creating a FrozenSet

```python
# Create a set
numbers = {1, 2, 3, 4, 5, 6}
print(numbers)

# Create a FrozenSet from a list
vowels = ["a", "e", "i", "o", "u"]
fSet = frozenset(vowels)
print(fSet)

# Create a FrozenSet from a tuple
vowels = ("a", "e", "i", "o", "u")
print(vowels)

# Create a FrozenSet from a dictionary
person = {"name": "John", "age": 23, "sex": "male"}
fSet = frozenset(person)
print(fSet)
```

**[⬆ Back to Top](#table-of-contents)**

#### FrozenSet Methods and Examples

```python
# copying a frozen set
vowels = ("a", "e", "i", "o", "u")
fSet = frozenset(vowels)
fSet1 = fSet.copy()
print(fSet1)

# difference of two frozen sets
set1 = frozenset([1, 2, 3, 4])
set2 = frozenset([3, 4, 5, 6])
set3 = set1.difference(set2)
print(set3)

# intersection of two frozen sets
set1 = frozenset([1, 2, 3, 4])
set2 = frozenset([3, 4, 5, 6])
set3 = set1.intersection(set2)
print(set3)

# checking if two frozen sets are disjoint
set1 = frozenset([1, 2, 3, 4])
set2 = frozenset([5, 6, 7, 8])
print(set1.isdisjoint(set2))

# check if one frozen set is a subset of another
set1 = frozenset([1, 2, 3, 4])
set2 = frozenset([1, 2, 3, 4, 5])
set3 = frozenset([1, 2, 3])
print(set2.issubset(set1))
print(set3.issubset(set1))

# check if one frozen set is a superset of another
set1 = frozenset([1, 2, 3, 4])
set2 = frozenset([1, 2, 3, 4, 5])
set3 = frozenset([1, 2, 3])
print(set1.issuperset(set2))
print(set1.issuperset(set3))

# symmetric difference of two frozen sets
set1 = frozenset([1, 2, 3, 4])
set2 = frozenset([3, 4, 5, 6])
set3 = set1.symmetric_difference(set2)
print(set3)

# union of two frozen sets
set1 = frozenset([1, 2, 3, 4])
set2 = frozenset([3, 4, 5, 6])
set3 = set1.union(set2)
print(set3)
```

## **[⬆ Back to Top](#table-of-contents)**

## Dictionary

A dictionary in Python is a collection of key-value pairs. Each key in a dictionary must be unique, and it is associated with a corresponding value. Dictionaries are defined using curly braces `{}` and the key-value pairs are separated by colons. Here are some dictionary syntax examples:

1. Basic Dictionary:

```python
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
```

2. Dictionary with Different Data Types:

```python
person = {'name': 'Alice', 'age': 30, 'is_student': False}
```

3. Nested Dictionary (Dictionary of Dictionaries):

```python
students = {
    'student1': {'name': 'Bob', 'age': 25},
    'student2': {'name': 'Charlie', 'age': 28}
}
```

4. Accessing Values by Key:

```python
person = {'name': 'Alice', 'age': 30}
name = person['name']
age = person['age']
```

5. Adding a New Key-Value Pair:

```python
person = {'name': 'Alice', 'age': 30}
person['city'] = 'New York'
```

6. Modifying a Value:

```python
person = {'name': 'Alice', 'age': 30}
person['age'] = 31
```

7. Dictionary with Various Data Types as Values:

```python
data = {'name': 'John', 'age': 25, 'grades': [90, 85, 92]}
```

8. Using Dictionary Methods (e.g., `keys()`, `values()`, `items()`):

```python
person = {'name': 'Alice', 'age': 30}
keys = person.keys()
values = person.values()
items = person.items()
```

9. Removing a Key-Value Pair:

```python
person = {'name': 'Alice', 'age': 30}
removed_value = person.pop('age')
```

10. Dictionary Comprehension:

```python
numbers = {'one': 1, 'two': 2, 'three': 3}
squared_numbers = {key: value ** 2 for key, value in numbers.items()}
```

**[⬆ Back to Top](#table-of-contents)**

# Methods and Examples

1. `clear()` - Removes all the elements from the dictionary:

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.clear()
print(my_dict)  # Output: {}
```

2. `copy()` - Returns a copy of the dictionary:

```python
original_dict = {'name': 'Alice', 'age': 30}
copied_dict = original_dict.copy()
print(copied_dict)  # Output: {'name': 'Alice', 'age': 30}
```

3. `fromkeys()` - Returns a dictionary with the specified keys and value:

```python
keys = ['a', 'b', 'c']
value = 0
new_dict = dict.fromkeys(keys, value)
print(new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}
```

4. `get()` - Returns the value of the specified key:

```python
my_dict = {'name': 'Bob', 'age': 25}
age = my_dict.get('age')
print(age)  # Output: 25
```

5. `items()` - Returns a list containing a tuple for each key-value pair:

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
items = my_dict.items()
print(items)  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])
```

6. `keys()` - Returns a list containing the dictionary's keys:

```python
my_dict = {'name': 'Charlie', 'age': 28, 'location': 'XYZ'}
keys = my_dict.keys()
print(keys)  # Output: dict_keys(['name', 'age', 'location'])
```

7. `pop()` - Removes the element with the specified key:

```python
my_dict = {'x': 10, 'y': 20, 'z': 30}
value = my_dict.pop('y')
print(value)  # Output: 20
print(my_dict)  # Output: {'x': 10, 'z': 30}
```

8. `popitem()` - Removes the last inserted key-value pair:

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
removed_item = my_dict.popitem()
print(removed_item)  # Output: ('c', 3)
print(my_dict)  # Output: {'a': 1, 'b': 2}
```

9. `setdefault()` - Returns the value of the specified key. If the key does not exist, inserts the key with the specified value:

```python
my_dict = {'name': 'Eve'}
age = my_dict.setdefault('age', 22)
print(my_dict)  # Output: {'name': 'Eve', 'age': 22}
```

10. `update()` - Updates the dictionary with the specified key-value pairs:

```python
my_dict = {'a': 1, 'b': 2}
my_dict.update({'b': 3, 'c': 4})
print(my_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}
```

11. `values()` - Returns a list of all the values in the dictionary:

```python
my_dict = {'x': 10, 'y': 20, 'z': 30}
values = my_dict.values()
print(values)  # Output: dict_values([10, 20, 30])
```

## **[⬆ Back to Top](#table-of-contents)**

## Functions and Exception Handling

### Functions

**Definition:** Functions are blocks of reusable code that perform a specific task. They help in organizing code and making it more modular.

**Clarification:** Functions allow you to define a set of instructions that can be executed whenever needed. They take input arguments, process them, and return an output. This makes your code easier to read, maintain, and debug.

**Syntax:**

```python
def function_name(parameter1, parameter2, ...):
    # Function body
    # Code to perform the task
    return result  # Optional
```

**Simple Example:**

```python
def greet(name):
    return "Hello, " + name + "!"

message = greet("Alice")
print(message)  # Output: Hello, Alice!
```

**Complex Example:**

```python
def calculate_total(price, quantity, tax_rate=0.1):
    subtotal = price * quantity
    tax_amount = subtotal * tax_rate
    total = subtotal + tax_amount
    return total

item_price = 25
item_quantity = 2
final_total = calculate_total(item_price, item_quantity)
print("Total:", final_total)  # Output: Total: 55.0
```

**[⬆ Back to Top](#table-of-contents)**

### Positional Arguments

**Definition:** Positional arguments are values or variables passed to a function in a specific order. They are matched with function parameters based on their positions.

**Clarification:** When calling a function with positional arguments, their order matters. The first argument is assigned to the first parameter, the second argument to the second parameter, and so on.

**Syntax:**

```python
function_name(arg1, arg2, ...)
```

**Example:**

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8
```

**[⬆ Back to Top](#table-of-contents)**

### Keyword Arguments

**Definition:** Keyword arguments are values or variables passed to a function using parameter names as keys. This allows you to specify which argument corresponds to which parameter, regardless of their positions.

**Clarification:** Keyword arguments enhance the clarity of function calls, especially when dealing with functions that have many parameters. They make the code more readable and less prone to errors caused by misplaced arguments.

**Syntax:**

```python
function_name(param1=value1, param2=value2, ...)
```

**Example:**

```python
def divide(dividend, divisor):
    return dividend / divisor

result = divide(dividend=10, divisor=2)
print(result)  # Output: 5.0
```

**[⬆ Back to Top](#table-of-contents)**

### Default Arguments

**Definition:** Default arguments are values assigned to function parameters during function definition. If a value is not provided for that parameter when calling the function, the default value is used.

**Clarification:** Default arguments allow you to make certain parameters optional. If a value is provided, it overrides the default; otherwise, the default value is used.

**Syntax:**

```python
def function_name(param1=default_value1, param2=default_value2, ...):
    # Function body
```

**Example:**

```python
def power(base, exponent=2):
    return base ** exponent

result1 = power(3)
result2 = power(2, 3)
print(result1)  # Output: 9
print(result2)  # Output: 8
```

**[⬆ Back to Top](#table-of-contents)**

### Gather Positional Arguments `*`

**Definition:** The asterisk (\*) is used in a function parameter to gather any remaining positional arguments into a tuple. This allows a function to accept a variable number of arguments.

**Clarification:** The gathered positional arguments are collected into a tuple. This is useful when you're not sure how many arguments will be passed to the function.

**Syntax:**

```python
def function_name(arg1, arg2, *args):
    # Function body
```

**Example:**

```python
def concatenate(separator, *strings):
    return separator.join(strings)

result = concatenate("-", "a", "b", "c")
print(result)  # Output: a-b-c
```

**[⬆ Back to Top](#table-of-contents)**

### Gather Keyword Arguments `**`

**Definition:** The double asterisk (\*\*) is used in a function parameter to gather any remaining keyword arguments into a dictionary. This allows a function to accept a variable number of keyword arguments.

**Clarification:** The gathered keyword arguments are collected into a dictionary. This is useful when you want to pass a varying number of named arguments to a function.

**Syntax:**

```python
def function_name(arg1, arg2, **kwargs):
    # Function body
```

**Example:**

```python
def display_info(**details):
    for key, value in details.items():
        print(key + ": " + value)

display_info(name="Alice", age="30", city="New York")
# Output:
# name: Alice
# age: 30
# city: New York
```

---

**[⬆ Back to Top](#table-of-contents)**

## License

This project is licensed under the [MIT License](LICENSE).
