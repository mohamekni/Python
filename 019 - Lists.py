# Lists

# [1] Lists Items Are Enclosed in Square Brackets
# [2] Lists Are Ordered, To Use Index To Access Item
# [3] List Are Mutable => Add, Delete, Edit
# [4] List Items Is Not Unique
# [5] List Can Have Different Data Types

myList = ["One", "Two", "One", 1, 100.5, True]

print(myList)  # Whole List
print(myList[1])  # "Two"
print(myList[-1])  # True
print(myList[-3])  # 1
print(myList[2:5])  # ['One', 1, 100.5]
print(myList[5])  # True
print(myList[::1])  # ['One', 'Two', 'One', 1, 100.5, True]
print(myList[::2])  # ['One', 1, True]


myList[2] = "Three"
myList[0:3] = ["A", "B", "C"]
print(myList)  # ['A', 'B', 'C', 1, 100.5, True]