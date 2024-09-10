import os

# path = "D:\Games\Left 4 Dead 2\left4dead2"

# if os.path.exists(path):
#     print("That location exists.")
#     if os.path.isfile(path):
#         print("It is a file.")
#     if os.path.isdir(path):
#         print("It is a directory.")
# else:
#     print("That location does not exist.")

#^ File Reading
# try:
#     with open('demo.txt') as file:
#         print(file.read())
#         print(file.closed)
# except FileNotFoundError:
#     print("There is no such file or directory.Try again!")
# else:
#     print("This file or directory exists :)")

#& File writing
# text = "Yooooooooo\nYou just wrote a file, LOL.\n"
# with open('demo.txt', 'w') as file:
#     file.write(text)
# write = "CYA!"
# with open('demo.txt', 'a') as file:
#     file.write(write)

#* Copying  a file
# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)
import shutil
shutil.copyfile("demo.txt", "copy.txt") #src.dst