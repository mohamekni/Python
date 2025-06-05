# Dictionary Methods


# clear()
user = {
    "name": "MohaSoGoodNoLove",
    "age": 23,
    "country": "grece",
}
user.clear()
print(user)  # {}


# update()
member = {
    "name" : "Mohamed"
}
member["proffession"] = "Programmer"
print(member)  # {'name': 'Mohamed', 'proffession': 'Programmer'}
member.update({"age": 23})
print(member)  # {'name': 'Mohamed', 'proffession': 'Programmer', 'age': 23}



# copy()
main = {
    "games" : "League Of Legends",
    "price" : "Free"
}
b = main.copy()
main.clear()
print(main)  # {}
print(b)  # {'games': 'League Of Legends', 'price': 'Free'}



# keys() + values()
print(b.keys())
print(b.values())
