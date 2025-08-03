# Built In Function => Filter

# [1] Filter Take A Function + Iterator
# [2] Filter Run A Function On Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function
# [4] Filter Out All Elements For Which The Function Return True
# [5] The Function Need To Return Boolean Value

# Example 1 

def checkNumber(num):
    if num > 20:
        return num
    
myNumbers = [10, 20, 30, 40, 50, 60, 70]
result = filter(checkNumber, myNumbers)
for number in result:
    print(number)


# Example 2

def checkName(name):
    if name.startswith('M'):
        return name
    
myNames = ["Mohamed", "Polak" , "Moha"]
result = filter(checkName, myNames)
for name in result:
    print(name)


# Example 3
    
myTexts = ["Mohamed", "Polak" , "Moha"]

for name in filter(lambda name: name.startswith('M'), myTexts):
    print(name)