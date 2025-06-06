# Comparison Operators


# [ == ] Equal
# [ != ] Not Equal
# [ > ] Greater Than
# [ < ] Less Than
# [ >= ] Greater Than or Equal
# [ <= ] Less Than or Equal


# Equal + Not Equal
print(100 == 100)   # True
print(100 == 200)   # False
print(100 == 100.00) # True

print(100 != 100)   # False
print(100 != 200)   # True
print(100 != 100.00) # False


# Greater Than + Less Than
print(100 > 100.00)   # False
print(100 > 200)   # False
print(100 > 50)    # True

print(100 < 100.00)   # False
print(100 < 200)   # True
print(100 < 50)    # False


# Greater Than or Equal + Less Than Or Equal
print(100 >= 100.00)   # True
print(100 >= 200)      # False
print(100 >= 50)       # True

print(100 <= 100.00)   # True
print(100 <= 200)      # True
print(100 <= 50)       # False