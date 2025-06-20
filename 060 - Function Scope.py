# Function Scope


x = 1 # Global Scope
def one():
    global x
    x = 2
    print(f'Variable From Function Scope {x}')

def two():
    global x
    x = 4
    print(f'Variable From Function Scope {x}')


one()
two()
print(f'Variable From Global Scope {x}')