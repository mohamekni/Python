# Tuples And Methods


# Tuple of One Element

tupleOne = ('Mohamed') 
tupleTwo = 'Mohamed'
print(type(tupleOne)) # <class 'str'>
print(type(tupleTwo)) # <class 'str'>

tupleOne = ('Mohamed',) 
tupleTwo = 'Mohamed',
print(type(tupleOne)) # <class 'tuple'>
print(type(tupleTwo)) # <class 'tuple'>


# Tuple Concatenation
a = (1,2,3,4,5)
b = (6,7,8,9,10)
c = a + b
print(c) # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(len(c)) # 10


# Tuple, List, String Repetition (*)
myString = "Mohamed"
myList = [1,2]
myTuple = ('Mohamed', 'Mekni')

print(myString * 2) # MohamedMohamed
print(myList * 2) # [1, 2, 1, 2]
print(myTuple * 2) # ('Mohamed', 'Mekni', 'Mohamed', 'Mekni')


# Methods => count()
x = (1,2,3,4,5,9,9,7,8,9)
print(x.count(9)) # 3


# Method => index()
a = (1,2,3,4,5,9,9,7,8,9)
print("The Position of Number 3 Is : {:d}".format(a.index(3))) # 2
print(f"The Position of Number 9 Is : {a.index(9)}") # 5


# Tuple Destruct
a = ('A','B',4,'C')
X, Y, _, Z,= a
print(X) # A
print(Y) # B
print(Z) # C