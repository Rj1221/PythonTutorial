# Break Statement is used to break the loop and continue statement is used to skip the current iteration and continue with the next iteration.

# Break Statement

# for i in range(1, 11):
#     print(i, end=" ")
#     if i == 5:
#         break
#     else:
#         print("else block")
# print("outside for loop")


# num = int(input("Enter a number to print Table: "))
# for i in range(1,20):
#     if i == 11:
#         break
#     else:
#         print(num,"x",i,"=",num*i)

# # Output:
# # Enter a number to print Table: 5
# # 5 x 1 = 5
# # 5 x 2 = 10
# # 5 x 3 = 15
# # 5 x 4 = 20
# # 5 x 5 = 25
# # 5 x 6 = 30
# # 5 x 7 = 35
# # 5 x 8 = 40
# # 5 x 9 = 45
# # 5 x 10 = 50 It will come out of the loop after 10
        
# Continue Statement is used to skip the current iteration and continue with the next iteration.

num=int(input("Enter a number to print Table: "))
for i in range(1, 13):
    if i == 10:
        continue  # skip the current iteration and continue with the next iteration means it will skip 10 and continue with 11
    else:
        print(num,"x",i,"=",num*i)

# Output:
# Enter a number to print Table: 5
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# Skip 10
# 5 x 11 = 55
# 5 x 12 = 60
# outside for loop
