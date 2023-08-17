# FrozenSet is immutable, so it can't be changed after it's created.
# It's hashable and can be used as a key in a dictionary.
# It's a set, so it can't contain duplicate elements.
# It's unordered, so it can't be indexed.
# It can be created from a set or any iterable object.
# It can be created with the built-in frozenset() function.
# It can be created with a literal syntax of {1, 2, 3}.

# In[ ]:

# Example 1: Create a FrozenSet from a set
# Create a set
numbers = {1, 2, 3, 4, 5, 6}
print(numbers)  # Output: {1, 2, 3, 4, 5, 6}

# Example 2: Create a FrozenSet from a list
# Create a list
vowels = ["a", "e", "i", "o", "u"]
print(vowels)  # Output: ['a', 'e', 'i', 'o', 'u']
fSet = frozenset(vowels)
print(fSet)  # Output: frozenset({'a', 'e', 'i', 'o', 'u'})
# fSet.add("p")  # AttributeError: 'frozenset' object has no attribute 'add'

# Example 3: Create a FrozenSet from a tuple
# Create a tuple
vowels = ("a", "e", "i", "o", "u")
print(vowels)  # Output: ('a', 'e', 'i', 'o', 'u')

# Example 4: Create a FrozenSet from a dictionary
# Create a dictionary
# random dictionary
person = {"name": "John", "age": 23, "sex": "male"}

fSet = frozenset(person)
print(
    "The frozen set is:", fSet
)  # The frozen set is: frozenset({'name', 'sex', 'age'})

# FrozenSet Methods
# Method	Description
# copy()	Returns a shallow copy of the frozen set.
# difference()	Returns the difference of two or more sets as a new set.
# intersection()	Returns the intersection of two sets as a new set.
# isdisjoint()	Returns True if two sets have a null intersection.
# issubset()	Returns True if another set contains this set.
# issuperset()	Returns True if this set contains another set.
# symmetric_difference()	Returns the symmetric difference of two sets as a new set.
# union()	Returns the union of sets in a new set.

# Example of FrozenSet Methods
# Example 1: copy()
# vowels tuple
vowels = ("a", "e", "i", "o", "u")
fSet = frozenset(vowels)
print(
    "The frozen set is:", fSet
)  # The frozen set is: frozenset({'a', 'e', 'i', 'o', 'u'})

# copying a frozen set
fSet1 = fSet.copy()
print(
    "The copied frozen set is:", fSet1
)  # The copied frozen set is: frozenset({'a', 'e', 'i', 'o', 'u'})

# Example 2: difference()
# random frozen set
set1 = frozenset([1, 2, 3, 4])
set2 = frozenset([3, 4, 5, 6])

# difference of two sets
set3 = set1.difference(set2)
print(set3)  # frozenset({1, 2})

# Example 3: intersection()
# random frozen sets
set1 = frozenset([1, 2, 3, 4])
set2 = frozenset([3, 4, 5, 6])

# intersection of two sets
set3 = set1.intersection(set2)
print(set3)  # frozenset({3, 4})

# Example 4: isdisjoint()
# random frozen sets
set1 = frozenset([1, 2, 3, 4])
set2 = frozenset([5, 6, 7, 8])

# checking if two sets are disjoint
print(set1.isdisjoint(set2))  # True

# Example 5: issubset()
# random frozen sets
set1 = frozenset([1, 2, 3, 4])
set2 = frozenset([1, 2, 3, 4, 5])
set3 = frozenset([1, 2, 3])

# check if set2 is a subset of set1
print(set2.issubset(set1))  # False

# check if set3 is a subset of set1
print(set3.issubset(set1))  # True

# Example 6: issuperset()
# random frozen sets
set1 = frozenset([1, 2, 3, 4])
set2 = frozenset([1, 2, 3, 4, 5])
set3 = frozenset([1, 2, 3])

# check if set1 is a superset of set2
print(set1.issuperset(set2))  # False

# check if set1 is a superset of set3
print(set1.issuperset(set3))  # True

# Example 7: symmetric_difference()
# random frozen sets
set1 = frozenset([1, 2, 3, 4])
set2 = frozenset([3, 4, 5, 6])

# symmetric difference of two sets
set3 = set1.symmetric_difference(set2)
print(set3)  # frozenset({1, 2, 5, 6})

# Example 8: union()
# random frozen sets
set1 = frozenset([1, 2, 3, 4])
set2 = frozenset([3, 4, 5, 6])

# union of two sets
set3 = set1.union(set2)
print(set3)  # frozenset({1, 2, 3, 4, 5, 6})

# Example 9: frozenset() with an iterable
# vowels tuple
vowels = ("a", "e", "i", "o", "u")
fSet = frozenset(vowels)
print(
    "The frozen set is:", fSet
)  # The frozen set is: frozenset({'a', 'e', 'i', 'o', 'u'})
