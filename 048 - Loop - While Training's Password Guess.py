# Loop => While Training


tries = 3
MainPass = "Moha1234"
inputPass = input('Tapez Votre Mot De Passe :')

while inputPass != MainPass :
    
    print(f'Il Reste {'une seule' if tries == 1 else tries} Fois')
    inputPass = input('Ressayer du tapez :')
    tries -= 1
    
    if tries == 0 :
        break
    
else :
    print("Correct Password !")