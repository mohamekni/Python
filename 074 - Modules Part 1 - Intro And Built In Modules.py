# Modules => Built In Modules

# [1] Module is A File Contain A Set Of Functions
# [2] You Can Import Module in Your App To Help You
# [3] You Can Import Multiple Modules
# [4] You Can Create Your Own Modules
# [5] Modules Saves Your Time

# Import Main Module

# import random
# x = random.random() * 20
# print(f"Print Random Float Number {x}")

# Show All Functions Inside Module
# import random
# print(dir(random))


# Import One or Two Functions From Module
from random import randint, randrange, random
print(f"Print Random Float {random()}")
print(f"Print Random Integer {randint(1,20)}")
