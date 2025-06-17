# Loop => For


mySkills = {
    "HTML" : "95%",
    "JS" : "90%",
    "PYTHON" : "80%",
    "CSS" : "70%"
}

for key in mySkills :
    print(f"{key} => {mySkills[key]}")


for key , value in mySkills.items() :
    print(f"{key} => {value}")

myUltimateSkills = {
    "HTML": {
        "Main":"80%",
        "PugJS" : "80%"
    },
    "css": {
        "Main":"80%",
        "saas" : "80%"
    }
}
for key , value in myUltimateSkills.items():
    for child_key, child_value in value.items():
        print(f"{child_key} => {child_value}")
