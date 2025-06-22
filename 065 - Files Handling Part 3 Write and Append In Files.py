# File Handling => Write and Append in File


myFile = open(r"C:\Users\MSI\Desktop\Programming\Python\nfiles\python.txt","w")

myFile.write("[1] - HTML \n   \
[2] - CSS                \n   \
[3] - JavaScript         \n   \
[4] - Python             \n   \
[5] - Java               \n   \
[6] - PHP                \n   \
[7] - C                  \n   \
[8] - C#")


myFile = open(r"C:\Users\MSI\Desktop\Programming\Python\nfiles\fun.txt","w")
myFile.write("MohaSoGoodNoLove\n" * 100)
myList = ["Mohamed" , "Ademo"]
myFile.writelines(myList)

myFile = open(r"C:\Users\MSI\Desktop\Programming\Python\nfiles\fun.txt","a")

myFile.write("\nLast Line\n\n\n ")