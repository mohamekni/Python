# Set Methods



# issuperset()
a = {1,2,3,4,5,6}
b = {1,2,3}
print(a.issuperset(b)) # True
print(b.issuperset(a)) # False


# issubset()
c = {1,2,3,4,5}
d = {1,2,3}
print(c.issubset(d)) # False
print(d.issubset(c)) # True


# isdisjoint()
e = {1,2,3}
f = {1,2,3,4,5,6}
x = {"Mohamed",}
print(e.isdisjoint(f)) # False
print(e.isdisjoint(x)) # True

