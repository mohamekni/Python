# Escape Sequences Characters
# \b => Back Space
# \newline => Escape New Line
# \ => Escape Back Slash
# \' => Escape Single Quotes
# \" => Escape Double Quotes
# \n => lINE Feed
# \r => Carriage Return
# \t => Horizantal Tab : Tabulation
# \xhh => Character Hex Value


# back Space
print("Hello\bWorld") # Will Remove 'o'

# Escape New Line
print("Hello \
I Love \
Python")

# Escape Back Slash
print("I Love Back Slash \\")

# Escape Single Quotes
print(' Hello \'World\'')

# Escape Double Quotes
print("Hello \"World\" ")

# lINE Feed
print("Hello World \nSecond Line")

# Carriage Return
print("123456\rAbcd") # Output 'Abcd56' Eliminer 4 First Character 

# Horizantal Tab
print("Hello\tPython")

# Character Hex Value
print("\x4D\x4F\x48\x41\x4D\x45\x44")