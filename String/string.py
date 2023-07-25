# ---------------------------------------------------------Single line string------------------------------------------

# name1 = "Raj"
# name2 = "Ramesh"
# print(name1 + name2) # Concatenation
# print('He said,"What\'s there?"')  # Escape sequence and string literal

# ---------------------------------------------------------Multiline string------------------------------------------

# apple = """Hey Raj
# How are you?
# Do you want to eat apple?
# """
# print(apple)  # Multiline string

# ---------------------------------------------------------String indexing------------------------------------------
# print(name1[0])  # Indexing
# print(name1[-1])  # Negative indexing
# Output: R
# Output: j

# ---------------------------------------------------------Looping through string------------------------------------------
# for character in apple:
#     print(character)

# Output: R
# Output: a
# Output: j

# ---------------------------------------------------------String slicing------------------------------------------
statement = "I Love My India"
print(statement[0:5])  # Slicing from 0 to 5 index (5 is excluded) means 0,1,2,3,4
# Output: I Lov
print(
    statement[0:5:2]
)  # Slicing from 0 to 5 index (5 is excluded) means 0,1,2,3,4 with step size 2 means 0,2,4
# Output: ILv
print(statement[0:])  # Slicing from 0 to end of string
# Output: I Love My India
