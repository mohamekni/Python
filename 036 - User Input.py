# User Input


FirstName = input('What\'s Your First Name :')
LastName = input('What\'s Your Last Name :')

FirstName = FirstName.strip().capitalize()  # strip() cancel spaces 
LastName = LastName.strip().capitalize() # capitalize() first character Uppercase
print(f"Your Name is {FirstName} {LastName}")