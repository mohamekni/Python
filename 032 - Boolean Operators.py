# Boolean


# and
# or
# not


age = 35
country = "Tunisia"
rank = 10

# and
print(age > 10 and country == "Tunisia" and rank > 5) # True
print(age > 10 and country == "Tunisia" and rank > 10) # False


# or
print(age > 40 or country == "France" or rank > 20) # False
print(age > 40 or country == "Tunisia" or rank > 20) # True


# not
print(age > 16) # True
print(not age > 16) # False
