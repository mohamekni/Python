# Control Flow
# if, Elif, Else
# Make Decisions


name = "Moha"
isStudent = True
Lprog = "Python"
price = 300
country = "France"
if country == 'Tunisia' or country == "France" :
    if isStudent:
        print(f"Hello {name} Because You Are Student Course Name {Lprog} Price {price - 90}")
    else :
        print(f"Hello {name} Course Name {Lprog} Price {price - 80}")
    
elif country == "Qatar" or country == "Grece" :
    print(f"Hello {name} Course Name {Lprog} Price {price - 50}")
else:
    print(f"Hello {name} Course Name {Lprog} Price {price - 20}")
