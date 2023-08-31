# How To store Sorted List Copy in another Variable

# Find Largest ,Smallest, Second Largest, Second Smallest in a list or Using 3 variables
# Using Variable

a = 10
b = 5
c = 7
list = [a, b, c]
print("Actual List is: ", list)
sorted_list = sorted(list)
# To Store the Sorted List Into a Variable We Should use sorted() Function not sort() Function
print("Sorted List is: ", sorted_list)
print("Largest Number is: ", sorted_list[-1])
print("Smallest Number is: ", sorted_list[0])
print("Second Largest Number is: ", sorted_list[-2])
