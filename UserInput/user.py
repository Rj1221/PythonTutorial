# input() function always returns a string
# a = input("Enter your name: ")
# print("Hello", a)


# x = input("Enter first number: ")
# y = input("Enter second number: ")
# z = x + y
# print(z)

# Output:
# Enter first number: 5
# Enter second number: 6
# 56 # This is not 11

# To convert string to integer, use int() function

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = x + y
print(z)
# Output:
# Enter first number: 5
# Enter second number: 6
# 11 # This is 11

# To convert string to float, use float() function

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = a + b
print(c)
# Output:
# Enter first number: 5.5
# Enter second number: 6.5
# 12.0 # This is 12.0
