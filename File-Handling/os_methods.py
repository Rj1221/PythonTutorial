import os

print("Current working directory:", os.getcwd())

# Change directory
os.chdir("C:/Users/.../Desktop")
print("Current working directory:", os.getcwd())

# List files and directories in current directory
print(os.listdir())

# Create a new directory
os.mkdir("new_dir")

# Rename a directory
os.rename("new_dir", "new_dir2")

# Remove a directory
os.rmdir("new_dir2")

# Create a new file
f = open("new_file.txt", "w")

# Rename a file
os.rename("new_file.txt", "new_file2.txt")

# Remove a file
os.remove("new_file2.txt")

# Check if a file exists
print(os.path.exists("new_file2.txt"))

# Check if a directory exists

print(os.path.exists("new_dir2"))

# Check if a path is a file or directory
print(os.path.isfile("new_dir2"))
print(os.path.isdir("new_dir2"))

# Get the size of a file

print(os.path.getsize("new_dir2"))

# Get the absolute path of a file
print(os.path.abspath("new_dir2"))
