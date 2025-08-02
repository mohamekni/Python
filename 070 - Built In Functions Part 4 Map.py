# Built In Functions Part 4 Map

# [1] Map Take A Function + Iterator
# [2] Map Called Map Because It Map The Function On Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function

# Use Map With Predefined Function

# def formatText(name):
#     return f"- {name.strip().capitalize()} -"

# myNames = ["Mohamed" , "Hamza" , "POLAK"]

# # myFormatedData = map(formatText,myNames)

# # print(myFormatedData)

# for name in map(formatText,myNames):
#     print(name)


# Use Map With Lambda Function

# def formatText(name):
#     return f"- {name.strip().capitalize()} -"

myNames = ["Mohamed" , "Hamza" , "POLAK"]

for name in list(map(lambda text: f"- {text.strip().capitalize()} -" ,myNames)):
    print(name)