# Strings Methods


# index(SubString, Start, End)
a = 'I Love Python'
# print(a.index("P")) # Index Number 7
# print(a.index("P", 0, 10)) # Index Number 7
# print(a.index("P", 0, 5)) # Through Error


# find(SubString, Start, End)
b = 'I Love Python'
print(b.find("P")) # Index Number 7
print(b.find("P", 0, 10)) # Index Number 7
print(b.find("P", 0, 5)) # -1


# rjust(Width, Fill Char) ljust(Width, Fill Char)
c = "Mohamed"
print(c.rjust(10))      #    Mohamed
print(c.rjust(10, "#")) # ###Mohamed

d = "Mohamed"
print(d.ljust(10))      # Mohamed   
print(d.ljust(10, "#")) # Mohamed###


# splitlines()
e = """First Line
Second Line
Third Line"""

print(e.splitlines()) # ['First Line', 'Second Line', 'Third Line']
print(type(e.splitlines())) # list

f = "FirstLine\nSecondLine\nThirdLine"
print(e.splitlines()) # ['First Line', 'Second Line', 'Third Line']


# expandtabs()
g = "I\tLove\tPython\tProgramming"
print(g.expandtabs(20)) #I                   Love                Python              Programming


# istitle()
one = 'I Love 5G'
two = 'I Love 5g'
print(one.istitle()) # True
print(two.istitle()) # False


# isspace()
three = " "
four = ""
print(three.isspace()) # True
print(four.isspace()) # False


# islower()
five = "I Love Python"
six = "i love python"
print(five.islower())   # False
print(six.islower())    # True


# isidentifier()
seven = "Mohamed_Mekni"
eight = "ILovePython100"
nine = "I Love-Python, A"
print(seven.isidentifier()) # True
print(eight.isidentifier()) # True
print(nine.isidentifier())  # False


# isalpha() (a=>z, A=>Z)
x = "AaaaaaBbbbbb"
y = "aaaaaa1bbbbbb"
print(x.isalpha()) # True
print(y.isalpha()) # False


# isalnum() (a=>z, A=>Z, 0=>9)
u = "AaaaaaBbbbbb"
v = "aaaaaa1bbbbbb"
print(u.isalnum()) # True
print(v.isalnum()) # True
