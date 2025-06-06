# Type Conversion


# str()
a = 10
print(type(a)) # <class 'int'>
print(type(str(a))) # <class 'str'>


# tuple()
# c = "Moha"                 # String
# d = [1,2,3]                # List 
# e = {"A" , "B" , "C"}      # Set
# f = {"One": 1, "Two": 2}   # Dictionary

# print(tuple(c)) # ('M', 'o', 'h', 'a')
# print(tuple(d)) # (1, 2, 3)
# print(tuple(e)) # ('B', 'C', 'A')
# print(tuple(f)) # ('One', 'Two')



# list()
# c = "Moha"                 # String
# d = (1,2,3)                # Tuple 
# e = {"A" , "B" , "C"}      # Set
# f = {"One": 1, "Two": 2}   # Dictionary

# print(list(c)) # ['M', 'o', 'h', 'a']
# print(list(d)) # [1, 2, 3]
# print(list(e)) # ['C', 'B', 'A']
# print(list(f)) # ['One', 'Two']



# set()
c = "Moha"                 # String
d = (1,2,3)                # Tuple 
e = ["A" , "B" , "C"]      # list
f = {"One": 1, "Two": 2}   # Dictionary

print(set(c)) # {'o', 'h', 'M', 'a'}
print(set(d)) # {1, 2, 3}
print(set(e)) # {'C', 'A', 'B'}
print(set(f)) # {'One', 'Two'}



# dict()
d = (("A",1),("B",2),("C",3))       # Tuple 
e = [["A",1] , ["B",2] ,["C",3]]    # list

print(dict(d)) # {'A': 1, 'B': 2, 'C': 3}
print(dict(e)) # {'A': 1, 'B': 2, 'C': 3}