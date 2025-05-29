# Lists Methods


# append()
myFriends = ["Rahma","Malek","Raoua"]
myFriends.append("Amir")
myFriends.append(True)
myFriends.append(False)
myFriends.append(1.99)
print(myFriends) # ['Rahma', 'Malek', 'Raoua', 'Amir', True, False, 1.99]

myOldFriends = ["Ademo","NOS"]
myFriends.append(myOldFriends)
print(myFriends) # ['Rahma', 'Malek', 'Raoua', 'Amir', True, False, 1.99, ['Ademo', 'NOS']]

print(myFriends[7][0]) # Ademo



# extend()
a = [1,2,3,4]
b = ["A","B","C"]
c = ["One","Two","Three"]
a.extend(b)
a.extend(c)
print(a) # [1, 2, 3, 4, 'A', 'B', 'C', 'One', 'Two', 'Three']



# remove()
x = [1, 2, 3, 4, 'A', 'B', 'C', 'One', 'Two', 'Three']
x.remove(1)
x.remove("A")
print(x) # [2, 3, 4, 'B', 'C', 'One', 'Two', 'Three']



# sort()
y = [-33 , 22 , 99 , 202 , -100 , 99.99]
y.sort(reverse=True)
print(y) # [202, 99.99, 99, 22, -33, -100]
y.sort()
print(y) # [-100, -33, 22, 99, 99.99, 202]
z = ["A","Z","C","D","E","F"]
z.sort()
print(z) # ['A', 'C', 'D', 'E', 'F', 'Z']



# reverse()
listOne = [1,2,3,4,5,6,7,8,9]
listTwo = ["A","B","C","D","E","F"]
listOne.reverse()
listTwo.reverse()
print(listOne) # [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(listTwo) # ['F', 'E', 'D', 'C', 'B', 'A']