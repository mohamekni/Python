# Set

# [1] Set Items Are Enclosed in Curly Braces {}
# [2] Set Items Are Not Ordered And Not Indexed
# [3] Set Indexing and Slicing Can't Be Done
# [4] Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List and Dict Are Not
# [5] Set Items Is Unique


# Not Ordered And Not Indexed
setOne = {1,2,3,4,5,6,"Mohamed"}
print(setOne)
# print(setOne[1]) # ERROR


# Slicing Can't Be Done
setTwo = {1,2,3,4,5,6}
print(setTwo)
# print(setTwo[0:3]) # ERROR


# Has Only Immutable Data Types
# setThree = {"Osama", 1, 2, 3, 4, 5, True, False, [1,2,3,4,5]} # unhashable type: 'list'
setThree = {"MohaSoGoodNoLove", 1, 2, 3, 4, 5, True, False, (1,2,3,4,5)}
print(setThree) # {False, 1, 2, 3, 4, 5, (1, 2, 3, 4, 5), 'Osama'}


# Set Items Is Unique
setFour = {1,2,3,4,5,1,1,1,2,1,1}
print(setFour) # {1, 2, 3, 4, 5}