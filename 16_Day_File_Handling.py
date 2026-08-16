# Day 16 - Creating and reading text files

# Writing to a text file
file = open("my_notes.txt", "w")
file.write("Day 16: Learning file handling in Python!\n")
file.write("Python makes working with files easy.\n")
file.close()
print("File created and text written successfully.")

# Reading the file back
file = open("my_notes.txt", "r")
content = file.read()
print("Reading file content:\n" + content)
file.close()