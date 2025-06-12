# Loop => While Training


# Empty List To Fill 
myFavoriteGames = []

# Max Games
maxGames = 5

while maxGames > 0 :

    myFavoriteGames.append(input('Tapez Votre Game: ').capitalize().lower())
    print(myFavoriteGames)
    print(f'Game Added, {maxGames - 1} Places Left')
    maxGames -= 1

else : 
    print('You List Is Full')

myFavoriteGames.sort()
index = 0
while index < len(myFavoriteGames) :
    print(f"{index + 1} {myFavoriteGames[index]}")
    index += 1