# Control Flow
# if, Elif, Else
# Make Decisions


name = "Moha"
prog = "Python"
price = 300
discountTN = 50
discountFR = 40
country = "France"
if country == 'Tunisia' :
    print(f"Hello {name} Course Name {prog} Price {price - discountTN}")
elif country == "France" :
    print(f"Hello {name} Course Name {prog} Price {price - discountFR}")
else :
    print(f"Hello {name} Course Name {prog} Price {price - 20}")
