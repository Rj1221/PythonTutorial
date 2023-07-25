# Assigning Tuples
# Tuples are immutable, which means you cannot change them once created.
l_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(l_tuple)
print(type(l_tuple))
# Accessing Tuple Elements
print(l_tuple[0])
print(l_tuple[1])
# Negative Indexing
print(l_tuple[-1])
print(l_tuple[-2])
# Range of Indexes
print(l_tuple[2:5])
print(l_tuple[:5])
# Loop Through a Tuple
for x in l_tuple:
    print(x, end=",")
print()
# Convert the tuple into a list to be able to change it
l_list = list(l_tuple)
l_list[0] = 11
l_tuple = tuple(l_list)
print("Converted to list from tuples:", l_tuple)
# Check if Item Exists
if 1 in l_tuple:
    print("Yes, '1' is in the tuple")
else:
    print("No, '1' is not in the tuple")

# Tuple Length
print("Length of tuple:", len(l_tuple))

# Add Items
# Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
# l_tuple[10] = 11  # TypeError: 'tuple' object does not support item assignment

# Remove Items
# Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely
# del l_tuple[0]  # TypeError: 'tuple' object doesn't support item deletion

# Join Two Tuples
l_tuple1 = (1, 2, 3)
l_tuple2 = (4, 5, 6)
l_tuple3 = l_tuple1 + l_tuple2
print("Join two tuples:", l_tuple3)


# Tuple Methods
# count()	Returns the number of times a specified value occurs in a tuple
print("Count of 1 in tuple:", l_tuple3.count(1))  # 1

# index()	Searches the tuple for a specified value and returns the position of where it was found
print("Index of 1 in tuple:", l_tuple3.index(1))  # 0

# Build in functions and operators
# all()	Returns True if all items in an iterable object are true
print("All items in tuple are true:", all(l_tuple3))  # True
# any()	Returns True if any item in an iterable object is true
print("Any item in tuple is true:", any(l_tuple3))  # True
# len()	Returns the length of an object
print("Length of tuple:", len(l_tuple3))  # 6
# max()	Returns the largest item in an iterable
print("Max item in tuple:", max(l_tuple3))  # 6
# min()	Returns the smallest item in an iterable
print("Min item in tuple:", min(l_tuple3))  # 1
# sum()	Returns the sum of all items in an iterable
print("Sum of all items in tuple:", sum(l_tuple3))  # 21
