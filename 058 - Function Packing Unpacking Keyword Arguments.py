# Function Packing Unpacking Keyword Arguments


mySkills = {
    "HTML":"50%",
    "CSS" :"90%",
    "JS":"70%" ,
    "Python" : "90%"
}

def show_skills(**skills):  # **

    print(type(skills))     # <class 'tuple'>

    for skill , value  in skills.items() :

        print(f"{skill} => {value}")

show_skills(HTML="50%" , CSS = "90%", JS="70%" , Python = "90%")
show_skills(**mySkills)