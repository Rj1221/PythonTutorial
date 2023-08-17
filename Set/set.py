# Set is a collection which is unordered and unindexed. No duplicate members.

# Creating a Set
# A set is created by using the set() function or placing all the elements within a pair of curly braces.

# It can have any number of items and they may be of different types (integer, float, tuple, string etc.). But a set cannot have a mutable element, like list, set or dictionary, as its element.

# # set of integers
# my_set = {1, 2, 3}
# print(my_set)

# # set of mixed datatypes
# my_set = {1.0, "Hello", (1, 2, 3)}
# print(my_set)

# # set cannot have duplicates
# my_set = {1,2,3,4,3,2}
# print(my_set)
# # Output: {1, 2, 3, 4}

# # we can make set from a list
# my_set = set([1,2,3,2])
# # Output: {1, 2, 3}

# Method Description
# add()	Adds an element to the set
# clear()	Removes all elements from the set
# copy()	Returns a copy of the set
# difference()	Returns the difference of two or more sets as a new set
# difference_update()	Removes all elements of another set from this set
# discard()	Removes an element from the set if it is a member. (Do nothing if the element is not in set)
# intersection()	Returns the intersection of two sets as a new set
# intersection_update()	Updates the set with the intersection of itself and another
# isdisjoint()	Returns True if two sets have a null intersection
# issubset()	Returns True if another set contains this set
# issuperset()	Returns True if this set contains another set
# pop()	Removes and returns an arbitary set element. Raise KeyError if the set is empty
# remove()	Removes an element from the set. If the element is not a member, raise a KeyError
# symmetric_difference()	Returns the symmetric difference of two sets as a new set
# symmetric_difference_update()	Updates a set with the symmetric difference of itself and another
# union()	Returns the union of sets in a new set
# update()	Updates the set with the union of itself and others

# Examples of Methods
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

# # clear my_set
# my_set.clear()
# print(my_set)  # Output: set()

# copy my_set
my_set2 = my_set.copy()
print(my_set2)  # Output: {1, 2, 3, 4, 5, 6, 8}

# pop an element
print(my_set2.pop())  # Output: 1

# remove an element
my_set2.remove(8)
print(my_set2)  # Output: {2, 3, 4, 5, 6}

# difference()
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}

# # set1 - set2
# print(set1.difference(set2))  # Output: {1, 2, 3}

# # set2 - set1
# print(set2.difference(set1))  # Output: {8, 6, 7}

# discard()
# set1 = {1, 2, 3, 4, 5}

# # removes element 5
# set1.discard(5)

# print(set1)  # Output: {1, 2, 3, 4}

# # removes element 6 (does not raise error)
# set1.discard(6)

# print(set1)  # Output: {1, 2, 3, 4}

# intersection()
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}

# # set1 intersection set2
# print(set1.intersection(set2))  # Output: {4, 5}

# # set2 intersection set1
# print(set2.intersection(set1))  # Output: {4, 5}

# # set1 & set2
# print(set1 & set2)  # Output: {4, 5}

# update()
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}

# # set1 intersection set2
# set1.intersection_update(set2)

# print(set1)  # Output: {4, 5}
