# List
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a)
print(type(a))
# Accessing List Elements
print(a[0])
print(a[1])
# Negative Indexing
print(a[-1])
print(a[-2])
# Range of Indexes
print(a[2:5])
print(a[:5])
# Change Item Value
a[0] = 11
print(a)
# Loop Through a List
for x in a:
    print(x, end=",")
print()
# Check if Item Exists
if 1 in a:
    print("Yes, '1' is in the list")
else:
    print("No, '1' is not in the list")
# List Length
print("Length of list:", len(a))
# Add Items
# append()	Adds an element at the end of the list
a.append(11)
print(a)
# insert()	Adds an element at the specified position
a.insert(0, 0)
print(a)
# extend()	Add the elements of a list (or any iterable), to the end of the current list
b = [12, 13, 14, 15]
a.extend(b)
print(a)
# Remove Item
# remove()	Removes the item with the specified value
a.remove(0)
print(a)
# pop()	Removes the element at the specified position
a.pop(0)
print(a)
# del()	Removes the element at the specified position
del a[0]
print(a)
# del()	Deletes the list completely
# del a
# print(a)  # NameError: name 'a' is not defined
# clear()	Removes all the elements from the list
a.clear()
print(a)
# Join Two Lists
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [11, 12, 13, 14, 15]
c = a + b
print(c)
# Join Two Lists
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [11, 12, 13, 14, 15]
for x in b:
    a.append(x)
print(a)
# Join Two Lists
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [11, 12, 13, 14, 15]
a.extend(b)
print(a)
# Join Two Lists
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [11, 12, 13, 14, 15]
b.extend(a)
print(b)
# The list() Constructor
a = list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(a)
# List Methods
# append()	Adds an element at the end of the list
# insert()	Adds an element at the specified position
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# remove()	Removes the item with the specified value
# pop()	Removes the element at the specified position
# del()	Removes the element at the specified position and deletes the list completely
# clear()	Removes all the elements from the list
# count()	Returns the number of elements with the specified value
# sort()	Sorts the list
# reverse()	Reverses the order of the list
# copy()	Returns a copy of the list
# Build in functions and operators
# all()	Returns True if all items in an iterable object are true
# any()	Returns True if any item in an iterable object is true
# len()	Returns the length of an object
