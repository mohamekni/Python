# File Handling => Read File


myFile = open(r"C:\Users\MSI\Desktop\Programming\Python\nfiles\python.txt","r")
# print(myFile) # File Data Object
# print(myFile.name)
# print(myFile.mode)
# print(myFile.encoding)

# print(myFile.read())
# print(myFile.read(3))


# print(myFile.readline())
# print(myFile.readline())

# print(myFile.readlines())       # ['[1] - Python\n', '[2] - JavaScript\n', '[3] - Java\n', '[4] - PHP\n', '[5] - C#']
# print(type(myFile.readlines())) # <class 'list'>

for line in myFile :
    print(line)
    if line.startswith("[3]"):
        break

myFile.close()