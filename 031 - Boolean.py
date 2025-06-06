# Boolean

# [1] Boolean Values Are The Two Constant Objects False + True

name = " "
print(name.isspace()) # True
print(100 > 200) # False
print(100 > 100) # False
print(100 == 100) # True


# True Values
print(bool("Moha"))     # True
print(bool(100.5))      # True
print(bool([1,2,3,4]))  # True


# False Values
print(bool(""))         # False
print(bool(0))          # False
print(bool(''))         # False
print(bool(False))      # False
print(bool([]))         # False
print(bool(()))         # False
print(bool({}))         # False
print(bool(None))       # False