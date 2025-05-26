# Strings Methods


# split() rsplit()
a = "I Love Python and JavaScript and MySQL"
print(a.split()) # ['I', 'Love', 'Python', 'and', 'JavaScript', 'and', 'MySQL']
print(type(a.split())) # list

b = "I-Love-Python-and-JavaScript-and-MySQL"
print(b.split('-')) # ['I', 'Love', 'Python', 'and', 'JavaScript', 'and', 'MySQL']

c = "I-Love-Python-and-JavaScript-and-MySQL"
print(c.split('-',2)) # ['I', 'Love', 'Python-and-JavaScript-and-MySQL']

d = "I-Love-Python-and-JavaScript-and-MySQL"
print(d.rsplit("-",3)) # ['I-Love-Python-and', 'JavaScript', 'and', 'MySQL']

# center()
e = "Mohamed"
print(e.center(11))     #   Mohamed
print(e.center(11,"#")) # ##Mohamed##

# count()
f = "I Love Python and PHP Because Python is easy"
print(f.count("Python")) # 2
print(f.count("Python",0,23)) # 1

# swapcase()
g = 'I Love Python'
h = 'i lOVE pYTHON'
print(g.swapcase()) # i lOVE pYTHON
print(h.swapcase()) # I Love Python

# startswith()
k = 'I Love Python'
print(k.startswith("I")) # True
print(k.startswith("L")) # False
print(k.startswith("P",7,12)) # True

# endswith()
l = 'I Love Python'
print(l.endswith("n")) # True
print(l.endswith("N")) # False
print(l.endswith("e",2,6)) # True
