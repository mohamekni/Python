# File Handling

# "a"   Append          Open File For Appending Values, Create File If Not Exists
# "r"   Read            [Default Value] Open File For Read And Give Error If File Not Exists       
# "w"   Write           Open File For Writing, Create File If Not Exists
# "x"   Create File     Create File, Give Error If File Exists

# import os

# Main Current Working Directory
# print(os.getcwd())

# # Directory For The Opened File 
# print(os.path.dirname(os.path.abspath(__file__)))

# # Change Current Working Directory
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

# print(os.getcwd())

file = open(r"C:\Users\MSI\Desktop\Programming\Python\nfiles\python.txt")