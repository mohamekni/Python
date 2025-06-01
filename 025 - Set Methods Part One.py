# Set Methods

# clear()
a = {1,2,3}
a.clear()
print(a) # set()


# union()
b = {1, 2, 3}
c = {"Mohamed","LaSquale","Ademo"}
d = {True , False}
print(b | c | d) # {False, 1, 2, 3, 'LaSquale', 'Mohamed', 'Ademo'}
print(b.union(c,d)) # {False, 1, 2, 3, 'LaSquale', 'Mohamed', 'Ademo'}


# add()
e = {1, 2, 3, 4}
e.add(5)
e.add(6)
print(e) # {1, 2, 3, 4, 5, 6}


# copy()
f = {1, 2, 3, 4}
g = f.copy()
print(g) # {1, 2, 3, 4}
g.add(5)
print(f) # {1, 2, 3, 4}
print(g) # {1, 2, 3, 4, 5}


# remove()
h = {1, 2, 3, 4, 5}
h.remove(5)
# h.remove(7) # ERROR
print(h) # {1, 2, 3, 4}


# discard() # if not found nothing happen
i = {1, 2, 3, 4, 5}
i.discard(6) # {1, 2, 3, 4, 5}
i.discard(5) # {1, 2, 3, 4}
print(i)


# pop() # Random Value
j = {"A", "B", "C"}
print(j.pop()) # C or A or B
print(j.pop()) # C or A or B
print(j.pop()) # C or A or B


# update()
k = {1,"Mohamed",2}
l = {"LaSquale","Ademo" ,1 ,2, 3, 4}
l.update(["v2v",667,"g2b"])
k.update(l)
print(k) # {1, 2, 3, 'Mohamed', 4, 'g2b', 'v2v', 'LaSquale', 'Ademo', 667}