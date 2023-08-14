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


countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Blastoff!")


user_input = ""
while user_input != "quit":
    user_input = input("Enter something (type 'quit' to exit): ")
    print("You entered:", user_input)



total = 0
num = int(input("Enter a number (enter a negative number to stop): "))
while num >= 0:
    total += num
    num = int(input("Enter a number (enter a negative number to stop): "))
print("Sum of the numbers:", total)
