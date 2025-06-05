# Dictionary

# [1] Dict Items Are Enclosed in Curly Braces
# [2] Dict Items Are Contains Key : Value
# [3] Dict Key Need To Be Immutable => (Number, String, Tuple) [] list not allowed
# [4] Dict Value Can Have Any Data Types
# [5] Dict Key Need To Be Unique
# [6] Dict Is Not Ordered You Access Its Element With Key



# Dictionary
user = {
    "name" : "Mohamed",
    "age" : 20,
    "country" : "Tunisia",
    "city" : "Bardo",
    (1,2,3) : "Test",
    "skills" : ["Html","Css","Python"],
    "rating" : 10.9,
    "rating" : 19
}
print(user['name'])
print(user.get('name'))
print(user.keys())
print(user.values())


# Two-Dimensional Dictionary
languages = {
    "One" : {
        'name' : 'HTML',
        'progress' : "80%"
    },
    'Two' : { 
        'name' : 'CSS',
        'progress' : "70%"
    },
    "Three" : {
        'name' : 'JS',
        'progress' : "60%"
    }
}
print(languages)
print(languages['Two']['progress'])
print(len(languages['One']))


frameWorkOne = {
    'name' : "Django",
    'progress' : "80%"
}
frameWorkTwo = {
    'name' : "Angular",
    'progress' : "90%"
}
frameWorkThree = {
    'name' : "ExpressJS",
    'progress' : "70%"
}
allFrameWork = {
    "One" : frameWorkOne,
    "Two" : frameWorkTwo,
    "Three" : frameWorkThree
}
print(allFrameWork)