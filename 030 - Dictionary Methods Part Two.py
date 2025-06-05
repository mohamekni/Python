# Dictionary Methods


# setdefault()
user = {
    "name" : "Mohamed"
}

print(user)
user.setdefault("Proffession", "Software Engineer")
print(user)


# popitem()
dictOne = {
    "games" : "GTA",
    "color" : "red"  
}
dictOne.update({"version" : 6})
print(dictOne)
print(dictOne.popitem()) # ('version', 6)


# items()
dictTwo = {
    "games" : "Vice City",
    "color" : "Light Blue"  
}
allItems = dictTwo.items()
dictTwo['Years'] = 50
print(allItems)


# formkeys()
games = ("LOL" , "TFT", "Valorant")
origin = "RIOT"
print(dict.fromkeys(games,origin))