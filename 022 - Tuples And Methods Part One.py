# Tuples

# [1] Tuples Items Are Enclosed in Parentheses
# [2] You Can Remove The Parentheses If You Want
# [3] Tuples Are Ordered, To Use Index To Access Item
# [4] Tuples Are Immutable => You Can't Add or Delete
# [5] Tuples Items Is Not Unique
# [6] Tuples Can Have Different Data Types
# [7] Operators Used in Strings and Lists Available In Tuples



myTupleOne = ("Mohamed" , "Mekni")
myTupleTwo = "Ademo" , "NOS"
print(type(myTupleOne)) # <class 'tuple'>
print(type(myTupleTwo)) # <class 'tuple'>


# Tuple Indexing
myTupleThree = (1,2,3,4,5)
print(myTupleThree[0]) # 1
print(myTupleThree[-1]) # 5
print(myTupleThree[-3]) # 3


# Tuple Assign Values
myTupleFour = (1,2,3,4,5)
# myTupleFour[2] = "Three"
# print(myTupleFour) # TypeError: 'tuple' object does not support item assignment ERROR


myTupleFive = ("Moha", "Moha", 1, 2, 3, True)
print(myTupleFive[0]) # Moha    
print(myTupleFive[1]) # Moha
print(myTupleFive[2:6]) # (1, 2, 3, True)

