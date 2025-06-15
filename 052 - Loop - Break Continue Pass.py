# Break, Continue, Pass


myNumber = [1,2,3,4,5]

# continue

for i in myNumber : 

    if i == 3 :

        continue

    print(i)

print('-' * 20)

# break

for n in myNumber : 

    if n == 3 :

        break

    print(n)

print('-' * 20)

# pass

for x in myNumber : 
    if x == 2 :
        pass
    print(x) # error
    