# Modules => Create Your Module


import sys
print(sys.path)

import mohasogoodnolove
# print(dir(mohasogoodnolove))

mohasogoodnolove.sayHello('Mohamed')
mohasogoodnolove.sayGoodbye('Mohamed')

# Alias
import mohasogoodnolove as fn
# print(dir(mohasogoodnolove))

fn.sayHello('Mohamed')
fn.sayGoodbye('Mohamed')

from mohasogoodnolove import sayHello
sayHello('Mohamed')