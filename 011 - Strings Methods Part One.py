# Strings Methods

# strip() rstrip() lstrip()
A = "    Mohamed    Mekni    "
print(A.strip())
print(A.rstrip())
print(A.lstrip())

B = "###Mohamed###Mekni###"
print(B.strip('#'))
print(B.rstrip('#'))
print(B.lstrip('#'))

# Title()
x = 'i love python and design and september'
print(x.title()) # I Love Python And Design And September

# Capitalize()
y = 'i Love python and design and September'
print(y.capitalize()) # I love python and design and september

# zfill()
a, b, c, d= "1","2","3","1111"
print(a.zfill(4)) # 0001
print(b.zfill(4)) # 0002
print(c.zfill(4)) # 0003
print(d.zfill(4)) # 1111

# upper()
first_name = "mohamed"
print(first_name.upper()) # MOHAMED

# lower()
last_name = "MOHASOGOODNOLOVE"
print(last_name.lower()) # mohasogoodnolove
