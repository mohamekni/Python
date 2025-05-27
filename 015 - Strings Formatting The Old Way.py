# String Formatting

# %s => String
# %d => Number
# %f => Float

name = "Mohamed"
age = 22
rank = 5
print("My Name is: "+ name) # My Name is: Mohamed
# print("My Name is: "+ name + "My Age is: "+age) # Type Error

print("My Name is: %s and my Age is: %d and my rank is: %f" % (name, age, rank)) # My Name is: Mohamed and my Age is: 22 and my rank is: 5.000000


a = "Mohamed"
b = "Python"
c = 10
print("My Name is %s I am %s Developer with %d Years Exp." % (a, b, c)) # My Name is Mohamed I am Python Developer with 10 Years Exp.


# Control Floating Point Number
myNumber = 10
print("My Number is: %d" % myNumber) # My Number is: 10
print("My Number is: %f" % myNumber) # My Number is: 10.000000
print("My Number is: %.2f" % myNumber) # My Number is: 10.00


# Truncate String
x = 'Hello World'
print('Hello %s' % x) # Hello Hello World
print('Hello %.5s' % x) # Hello Hello