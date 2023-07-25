# Over String
# name = "Python"
# For in loop is used to iterate over a sequence (list, tuple, string) or other iterable objects.
# for i in name:
#     print(i, end=",")  # This will print each character of string in new line with comma

# Over Tuple
# tup = (1, 2, 3, 4, 5)
# for i in tup:
#     print(i, end=",")  # End is used to print in same line

# Over List
# list1 = [1, 2, 3, 4, 5]
# for i in list1:
#     print(i, end=",")

# Example 2
# list2 = ["Python", "Java", "C++"]
# for i in list2:
#     print(i, end=",")

# Example 3
# list3 = ["Python", "Java", "C++"]
# for i in list3:
#     print(i, end=",")
#     for j in i:
#         print(j, end=",")


# Using range() function it will accept 3 arguments start, stop, step
# for i in range(10):  # This will print from 0 to 9 start from 0 and stop at 9
# print(i, end=" ")
# print()  # This will print in new line
# for i in range(1, 10):  # This will print from 1 to 9 start from 1 and stop at 9
# print(i, end=" ")
# print()
# for i in range(
# 1, 10, 2
# ):  # This will print from 1 to 9 start from 1 and stop at 9 with step 2
# print(i, end=" ")

# Over Dictionary
dict1 = {
    "name": "Python",
    "version": 3.8,
    "year": 1991,
    "creator": "Guido van Rossum",
    "address": {"permanent": "India", "temporary": "USA"},
}
for i in dict1:
    print(i, end=",")
    if i == "address":
        for j in dict1[i]:
            print(j, end=",")
            print(dict1[i][j], end=",")
            # for k in dict1[i][j]: # This will print each  and every character of string in new line with comma
            #     print(k, end=",")
print()
