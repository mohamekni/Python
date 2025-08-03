# Built In Function

# enumerate()
# help()
# reversed()


# enumerate(iterable + start=0)

mySkills = ['html', 'css', 'js']

mySkillsWithCounter = enumerate(mySkills)

for counter , item in mySkillsWithCounter:


    print(f"{counter} - {item}")


# help()
print(help(print))


# reversed(iterable)

myString = 'Moha'


for i in reversed(myString):
    print(i)