# Built In Functions

# sum()
# round()
# range()
# print()


# sum(iterable, start)
a = [1,10,50,44]
print(sum(a))       # 105
print(sum(a,50))    # 155

# round(number, numofdigits)
print(round(155.65))    # 156
print(round(155.45))    # 155
print(round(155.556, 2))    # 155.56

# range(start, end, step)
print(list(range(10)))      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(0,20,2)))  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# print()
print("Moha","La Squale", sep="|")
print("Moha La Squale")


print('First Line', end='\n') # Par Defaut
print('Second Line')