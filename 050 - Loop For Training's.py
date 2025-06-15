# Loop => For

# myRange = range(1,101)
# for i in myRange :
#     print(i)

mySkills = {
    "Html" : "90%",
    "CSS"  : "85%",
    "JS"  : "80%",
    "Python"  : "99%",
    "PHP"  : "70%",
    "Java"  : "80%",
}
print(mySkills['JS'])
print(mySkills.get("Python"))

for i in mySkills : 
    print(f"My Progress in Language {i} Is : {mySkills[i]}")