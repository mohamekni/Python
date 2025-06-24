# Built In Functions


# all()
# any()
# bin()
# id()

# a = [1, False , 3, 4]
# if all(a):
#     print('All Elements Is True')
# else :
#     print("One Is false")

b = [1, False , 3, 4]
if any(b):
    print('One Element Is True')
else :
    print("All Element Is False")

c = 100
print(bin(c))

x = 1
y = 2
print(id(x))
print(id(y))