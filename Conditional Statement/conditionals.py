# There are four types of conditional statements in Python:
# 1. if statement
# 2. if-else statement
# 3. if-elif-else statement
# 4. nested if statement

# Conditional Operators
# 1. == (equal to)
# 2. != (not equal to)
# 3. > (greater than)
# 4. < (less than)
# 5. >= (greater than or equal to)
# 6. <= (less than or equal to)

# if statement
# Syntax:
# if condition:
# statement(s)

# Example:
if 5 > 2:
    print("5 is greater than 2")

# if-else statement
# Syntax:
# if condition:
# statement(s)
# else:
# statement(s)

# Example:
if 5 < 2:
    print("5 is less than 2")
else:
    print("5 is greater than 2")

# if-elif-else statement
# Syntax:
# if condition:
# statement(s)
# elif condition:
# statement(s)
# else:
# statement(s)

# Example:
a = 5
b = 5
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is less than b")

# nested if statement
# Syntax:
# if condition:
# statement(s)
# if condition:
# statement(s)
# else:
# statement(s)

# Example:
a = 5
b = 5
if a > b:
    print("a is greater than b")
    if a == b:
        print("a is equal to b")
    else:
        print("a is less than b")
else:
    print("a is less than b")
