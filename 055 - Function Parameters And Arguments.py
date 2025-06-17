# Function Parameters And Arguments

a , b , c = "Moha" , "Ad" , "Le A"
# print(f"{a}")
# print(f"{b}")
# print(f"{c}")

# def                                   => Function Keyword [Define]
# say_Hello                             => Function Name
# name                                  => Parameter
# print(f"Hello My Name Is {name}")     => Task
# say_Hello("Mohamed")                  => Mohamed is The Argument

def say_Hello(name):
    print(f"Hello My Name Is {name}")


say_Hello(a)
say_Hello(b)
say_Hello(c)


def Addition(x, y) :
    return x + y
print(Addition(5,7))


def full_name(first,middle,last):
    print(f"Hello {first.strip().capitalize()} {middle.strip():.1s} {last.strip().capitalize()}")

full_name("Mohamed" , "Mekni" , "Freeze")