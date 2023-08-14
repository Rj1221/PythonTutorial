count = 1

while count <= 5:
    print(count)
    count += 1

# While loop with else

count = 1

while count <= 5:
    print(count)
    count += 1
else:
    print("Count is greater than 5")

# Countdown:

# Let's say you want to create a countdown from 5 to 1:
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Blastoff!")

# User Input:

# Here's an example where the program asks the user for input until they enter "quit":

user_input = ""
while user_input != "quit":
    user_input = input("Enter something (type 'quit' to exit): ")
    print("You entered:", user_input)


# Sum of Numbers:

# This example calculates the sum of numbers entered by the user until they enter a negative
total = 0
num = int(input("Enter a number (enter a negative number to stop): "))
while num >= 0:
    total += num
    num = int(input("Enter a number (enter a negative number to stop): "))
print("Sum of the numbers:", total)
