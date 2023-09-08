# Open a File
# with open("example.txt", "r") as f:
#     print(f.read())
# Open  will open a file in read mode by default
# w is used to write to a file and will overwrite the file if it already exists
# a is used to append to a file
# r+ is used to read and write to a file

open_file = open("example.txt", "r")
print(open_file.read())
write_file = open("example.txt", "w")
write_file.write("This is a new line")
open_file.close()
