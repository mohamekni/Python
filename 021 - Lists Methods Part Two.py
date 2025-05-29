# List Methods


# clear()
a = [1,2,3,4]
a.clear() 
print(a) # []


# copy()
b = [1,2,3,4]
c = b.copy()
print(c) # [1,2,3,4]


# count()
d = [1,2,3,4,5,4,4]
print(d.count(4)) # 3


# index()
e = [1,2,3,4,5,6]
print(e.index(5)) # 4
# print(e.index(4,5,7)) # ValueError


# insert()
f = [1,2,3,4,5,"A","B"]
f.insert(0,'Test')
print(f) # ['Test', 1, 2, 3, 4, 5, 'A', 'B']


# pop()
g = [1,2,3,4,5,"A","B"]
print(g.pop(2)) # 3
print(g) # [1, 2, 4, 5, 'A', 'B']


