# Practical Membership Control


# Admins
admins = ["Mohamed" , "Rahma" , "Ademo" , "Nos"]

name = input("Tapez Votre Nom : ").strip().capitalize()

# Update
if name in admins :
    print(f"Hello {name} You Are Admin")
    option = input("Delete Or Update Your Name : ").strip().capitalize()
    
    if option == "Update":
        theNewName = input("Tapez Votre Nouveau Nom : ")
        admins[admins.index(name)] = theNewName
        print(admins)
# Delete
    elif option == "Delete":
        admins.remove(name)
        print(admins)   
    else :
        print("Wrong Option Choosed")
elif name not in admins :
    status = input("Not Admin , Add You Y or N ? ").strip().capitalize()
    if status == "Yes" or status == "Y":
        admins.append(name)
        print(admins)
    else : 
        print("Try Again")