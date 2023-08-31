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
# Reverse the sorted_list variable and store it in another variable using reverse() function
reverse_list = sorted_list[::-1]  # Using Slicing Method to Reverse the List
print("Reverse List is: ", reverse_list)
name = "Sachin"
print(name[::-1])  # Reverse the String
# Sort and Reverse the List at same time
reverse_list = sorted(sorted_list, reverse=True)  # Using reverse=True
print("Reverse List is: ", reverse_list)
