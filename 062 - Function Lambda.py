# Function Lambda
# Anonymous Function


# [1] It Has No Name
# [2] You Can Call It Inline Without Defining It
# [3] You Can Use It Return Data From Another Function
# [4] Lambda Used For Simple Functions and Def Handle The Large Tasks
# [5] Lambda Is One Single Expression not block of code
# [5] Lambda type is Function



def say_Hello(name) : return f"Hello {name}"

hello = lambda name : f"Hello {name}"

print(say_Hello("MohaFreeze"))
print(hello("MohaSoGoodNoLove"))

print(say_Hello.__name__)   # say_Hello
print(hello.__name__)       # <lambda>

print(type(hello))          # <class 'function'>