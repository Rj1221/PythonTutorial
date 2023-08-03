# List of Operators in Python

# Arithmetic Operators

# Addition +
a = 10 + 20
# Subtraction -
b = 20 - 10
# Multiplication *
c = 10 * 20
# Division /
d = 20 / 10
# Modulus %
e = 20 % 10  # Remainder
# Exponent **
f = 10**2  # 10^2
# Floor Division // used to get the quotient
g = 20 // 10  # Quotient

a = divmod(9, 5)  # It is used to return the quotient and remainder of the division
print(a)  # (1, 4)

# Assignment Operators

# Equal =
h = 10
# Add and =
h += 10  # h=h+10
# Subtract and =
h -= 10  # h=h-10
# Multiply and =
h *= 10  # h=h*10
# Divide and =
h /= 10  # h=h/10
# Modulus and =
h %= 10  # h=h%10
# Exponent and =
h **= 10  # h=h**10
# Floor Division and =
h //= 10  # h=h//10

# Comparison Operators

# Equal ==
if 10 == 10:
    print("True")
# Not Equal !=
if 10 != 20:
    print("True")
# Greater Than >
if 10 > 5:
    print("True")
# Less Than <
if 10 < 20:
    print("True")
# Greater Than or Equal To >=
if 10 >= 10:
    print("True")
# Less Than or Equal To <=
if 10 <= 20:
    print("True")

# Logical Operators

# And and
if 10 == 10 and 20 == 20:
    print("True")
# Or or
if 10 == 10 or 20 == 20:
    print("True")
# Not not
if not 10 == 20:
    print("True")


# Identity Operators
# Example: is, is not
# Is is
if 10 is 10:
    print("True")

# Is Not is not
if 10 is not 20:
    print("True")


# Membership Operators
# Example: in, not in
# In in
l_list = [1, 2, 3, 4, 5]
if 1 in l_list:
    print("True")

# Not In not in
if 10 not in l_list:
    print("True")

# Bitwise Operators

# Example: &, |, ^, ~, <<, >>

# And &
# The code is performing a bitwise AND operation between the variables `a` and `b`.
# It first converts the numbers into binary, and then performs the AND operation.
a = 10
b = 20
c = a & b  # 0
print(c)

# Or |
# Used to perform bitwise or operation on the binary representation of the numbers
# It first converts the numbers into binary, and then performs the OR operation.
a = 10
b = 20
c = a | b  # 30

# Xor ^
# Used to perform bitwise XOR operation on the binary representation of the numbers
# It first converts the numbers into binary, and then performs the XOR operation.
a = 10
b = 20
c = a ^ b  # 30

# Not ~
a = 10
b = ~a

# Left Shift <<
# Used to perform left shift operation on the binary representation of the numbers
# It first converts the numbers into binary, and then performs the left shift operation.
a = 10
b = a << 2  # 40

# Right Shift >>
a = 10
b = a >> 2  # 2

# Operator Precedence
# ()
# **
# ~
# * / % //
# + -
# << >>
# Example
a = 10 + 20 * 30 / 40
# 10 + 600 / 40
