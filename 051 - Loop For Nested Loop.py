# Loop => For
# Nested Loop


# Friends = ["Ademo" , "NOS" , "LaSquale" , "SCH" , "Freeze Corleone"]
# Lang = ["HTML" , "CSS" , "Python"]

# for i in Friends : 
#     print("* "+i + " :")
#     for n in Lang :
#         print("- "+n)


Peoples = {
    "Freeze Corleone" : {
        "HTML" : "90%",
        "CSS"  : "85%",
        "JS"  : "85%"
    },
    "SCH" : {
        "HTML" : "90%",
        "CSS"  : "65%",
        "JS"  : "90%"
    },
    "Ademo" : {
        "HTML" : "60%",
        "CSS"  : "59%",
        "JS"  : "40%"
    },
    "NOS" : {
        "HTML" : "99%",
        "CSS"  : "50%",
        "JS"  : "70%"
    },
}
for i in Peoples :
    print(f"Hello {i} Your Skills Is :")
    for n in Peoples[i]:
        print(f"{n} : {Peoples[i][n]}")