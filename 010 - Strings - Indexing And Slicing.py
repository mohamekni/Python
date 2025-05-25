# Strings - Indexing And Slicing

# [1] All Data in Python Is Object
# [2] Object Contain Elements
# [3] Every Element Has Its Own Index
# [4] Python Use Zero Based Indexing (Index Start From Zero)
# [5] Use Square Brackets To Access Element 
# [6] Enable Accessing Parts Of Strings, Tuples or Lists


# Indexing ( Access Single Item)
myString = "I Love Python"
print(myString[0]) # Index 0 => I
print(myString[7]) # Index 0 => P

print(myString[-1]) # Index -1 => First Character From End
print(myString[-11]) # Index -11 => 11 Character From End

# Slicing (Access Multiple Sequence Items)
# [Start:End] End Not Included
# [Start:End;Steps]
print(myString[9:11]) # => th
print(myString[3:5]) # => ov

print(myString[:6]) # If Start Null Will Start From 0
print(myString[7:]) # If End Null Will Go To The End

print(myString[:]) # Full Data

print(myString[0::1]) # Full Data
print(myString[::1]) # Full Data
print(myString[::2]) # Step by 2