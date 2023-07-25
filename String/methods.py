# Strings are immutables
# -------------------------------------------------Methods-------------------------------------------------
str1 = "Hello World !!!"
print(str1.upper())  # Converts it into Upper Case
print(str1.lower())  # Converts it into Lower Case
print(str1.capitalize())  # Converts the first letter into Upper Case
print(str1.title())  # Converts the first letter of every word into Upper Case
print(str1.swapcase())  # Converts the Upper Case into Lower Case and vice versa
print(
    str1.replace("World", "Python")
)  # Replaces the first string with the second string
print(str1.count("l"))  # Counts the number of times the string is present
print(str1.startswith("H"))  # Checks if the string starts with the given string
print(str1.endswith("!!!"))  # Checks if the string ends with the given string
print(str1.find("World"))  # Finds the index of the given string
print(str1.rfind("World"))  # Last occurrence of the given string
print(str1.index("World"))  # Finds the index of the given string
print(
    str1.isalnum()
)  # Checks if the string is alphanumeric consists of (A-Z, a-z, 0-9)
print(str1.isalpha())  # Checks if the string is alphabetic consists of (A-Z, a-z)
print(str1.isnumeric())  # Checks if the string is numeric consists of (0-9)
print(str1.isdecimal())  # Checks if the string is decimal consists of (0-9)
print(str1.strip())  # Removes the white spaces from the string
print(str1.lstrip())  # Removes the white spaces from the left side of the string
print(str1.rstrip())  # Removes the white spaces from the right side of the string
print(str1.split(" "))  # Splits the string into a list
print(str1.center(50))  # Centers the string with the given width
print(str1.center(50, "*"))  # Centers the string with the given width and character
print(str1.islower())  # Checks if the string is in Lower Case
print(str1.isupper())  # Checks if the string is in Upper Case
print(str1.istitle())  # Checks if the string is in Title Case
print(str1.isprintable())  # Checks if the string is printable
print(str1.isspace())  # Checks if the string is a space
print(str1.join("Python"))  # Joins the string with the given string
