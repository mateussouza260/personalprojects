with open("/Users/mateu/Desktop/my_file.txt") as file:
    contents = file.read()
print(contents)

# mode w stands for write and can create a file if it doesn't exists. If it exists, the content will be erased and
# the a new one will be write
#
# mode a stands for append and don't erase what is written, just add. (don't forget the \n)

# with open("new_file.txt", mode="w") as file:
#     file.write("\nNew text.")
