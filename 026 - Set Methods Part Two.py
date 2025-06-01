# Set Methods


# difference()
a = {1, 2, 3, 4}
b = {1, 2, "Mohamed"}
print(a.difference(b)) # {3, 4}
print(b.difference(a)) # {"Mohamed"}


# difference_update()
c= {1, 2, 3, 4}
d = {1, 2, "Mohamed"}
c.difference_update(d)
print(c) # {3, 4}
print(d) # {1, 2, "Mohamed"}


# intersection()
e = {1, 2, 3 ,4 ,"Mohamed" , "X"}
f = {"X", "Mohamed", "Ademo"}
print(e.intersection(f)) # {"Mohamed", "X"}
print(e) # {1, 2, 3, 4, 'X', 'Mohamed'}


# intersection_update()
g = {1, 2, 3 ,4 ,"Mohamed" , "X"}
h = {"X", "Mohamed", "Ademo"}
print(g.intersection_update(h)) # None
print(g) # {'X', 'Mohamed'}


# symmetric_difference()
i = {1, 2, 3 ,4 ,"Mohamed" , "X"}
j = {"X", "Mohamed", "Ademo"}
print(i.symmetric_difference(j)) # {1, 2, 3, 4, 'Ademo'}
print(j.symmetric_difference(i)) # {1, 2, 3, 4, 'Ademo'}


# symmetric_difference_update()
k = {1, 2, 3 ,4 ,"Mohamed" , "X",667,"v2v"}
l = {1, 2, 3 ,4, "X", "Mohamed", "Ademo"}
k.symmetric_difference_update(l)
print(k) # {667, 'v2v', 'Ademo'}


