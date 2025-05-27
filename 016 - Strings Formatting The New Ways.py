# String Formatting


# {:s} => String
# {:d} => Number
# {:f} => Float

name = "Mohamed"
age = 22
rank = 10

print("My Name is: {}".format(name)) # My Name is: Mohamed
print("My Name is {} My Age is: {}".format(name, age)) # My Name is Mohamed My Age is: 22
print("My Name is {:s} My Age is: {:d} My Rank is: {:f}".format(name, age, rank)) # My Name is Mohamed My Age is: 22 My Rank is: 10


# control Floating Point Number
myNumber = 10
print("My Number is: {:d}".format(myNumber)) # My Number is: 10
print("My Number is: {:f}".format(myNumber)) # My Number is: 10.000000
print("My Number is: {:.2f}".format(myNumber)) # My Number is: 10.00


# truncate String
longString = 'Hello Iam Mohamed Iam Python Developer Iam an Engineering Studentent ' 
print("Message is {}".format(longString)) # Message is Hello Iam Mohamed Iam Python Developer Iam an Engineering Studentent 
print("Message is {:.5s}".format(longString)) # Message is Hello
print("Message is {:.17s}".format(longString)) # Message is Hello Iam Mohamed


# Format Money
myMoney = 4200000000
print('My Money in Bank Is: {}'.format(myMoney)) # My Money in Bank Is: 4200000000
print('My Money in Bank Is: {:_d}'.format(myMoney)) # My Money in Bank Is: 4_200_000_000
print('My Money in Bank Is: {:,d}'.format(myMoney)) # My Money in Bank Is: 4,200,000,000
# print('My Money in Bank Is: {:&d}'.format(myMoney)) # Wrong Format


# ReArrange Items
a , b , c = "One","Two","Three"
print("Hello {} {} {}".format(a, b, c)) # Hello One Two Three
print("Hello {2} {1} {0}".format(a, b, c)) # Hello Three Two One
print("Hello {1} {2} {0}".format(a,b,c)) # Hello Two Three One

x , y , z = 10,20,30
print("Hello {} {} {}".format(x, y, z)) # Hello 10 20 30
print("Hello {2:d} {1:d} {0:f}".format(x, y, z)) # Hello 30 20 10.000000
print("Hello {1:.2f} {2:.2f} {0:.2f}".format(x,y,z)) # Hello 20.00 30.00 10.00


# Format in Latest Version
myName = "Mohamed"
myAge = 22
print("My Name is: {myName} and My Age is: {myAge}") # My Name is: {myName} and My Age is: {myAge}
print(f"My Name is: {myName} and My Age is: {myAge}") # My Name is: Mohamed and My Age is: 22