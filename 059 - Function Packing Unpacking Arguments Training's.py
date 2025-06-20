# Function Packing Unpacking Arguments Training's
myTuple = ("HTML", "CSS", "JS")
mySkills = {
    "HTML":"50%",
    "CSS" :"90%",
    "JS":"70%" ,
    "Python" : "90%"
}

def show_skills(name, *skills, **skillsWithProgress):

    print(f"Hello {name} \nSkills :")

    for skill in skills :

        print(f"- {skill}")
    
    for key, value in skillsWithProgress.items():

        print(f"{key} => {value}")
        
show_skills("Mohamed",*myTuple,**mySkills)