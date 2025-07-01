# Built In Functions

# abs()
# pow()
# min()
# max()
# slice()


# abs()
print(abs(100))
print(abs(-100))
print(abs(10.09))
print(abs(-10.09))


# pow(base, exp, mod)
print(pow(2,3,5)) # (2*2*2) % 5 = 8 % 5 = 3


# min()
muNumber = [10,20,30,-10,-20,-30]
print(min(muNumber))
print(min('X','Y'))


# max()
print(max(muNumber))
print(max('X','Y'))


# slice(start, end, step)
list_char = ['A','B','C','D','E','F','G','H']
print(list_char[:5])
print(list_char[slice(2,5)])