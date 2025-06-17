# Function Packing, Unpacking Arguments *Args

# print(1, 2, 3, 4)
# myList = [1, 2, 3, 4]
# print(*myList)

def say_Hello(*peoples):
    for i in peoples:
        print(i)

say_Hello("Mohamed" , "Ademo" , "Nos" , "SCH")


def addition(*num):
    x = 0
    for i in num :
        x += i
    print(x)


addition(1,6,5,9)