# File Handling => Important Info


# myFile = open(r"C:\Users\MSI\Desktop\Programming\Python\nfiles\fun.txt","a")
# myFile.truncate(5)
# print(myFile.tell())        # Position cursor
myFile = open(r"C:\Users\MSI\Desktop\Programming\Python\nfiles\fun.txt","r")
myFile.seek(3)  # aSoGoodNoLove
print(myFile.read())

import os
os.remove(r"C:\Users\MSI\Desktop\Programming\Python\nfiles\python.txt")