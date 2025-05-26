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
x = "Mohamed"
print(x.center(11))
print(x.center(11,"#"))
