# Membership Operators
# in
# not in


# string
name = "MohaSoGoodNoLove"
print("M" in name) # True
print("E" in name) # False


# list
Friends = ["Mohamed" , "Zouhair" , "Ademo"]
print("Mohamed" in Friends) # True
print("Mohamed" not in Friends) # False


# Using in and not in with Condition
countryOne = ["France", "Germany" , "Qatar"]
Origin = "Qatar"
Discount = 80

if Origin in countryOne :
    print(f"You Have Discount {Discount}$")