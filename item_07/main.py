"""
7. Prefer enumerate over range
"""

# FIRST EXAMPLE
from random import randint

random_bits = 0
for i in range(32):
    if randint(0, 1):
        random_bits |= 1 << i

print(bin(random_bits))

# SECOND EXAMPLE
flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
for flavor in flavor_list:
    print(f'{flavor} is delicious')

# THIRD EXAMPLE
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print(f'{i + 1}: {flavor}')

# FOURTH EXAMPLE
for i, flavor in enumerate(flavor_list, 1):
    print(f'{i}: {flavor}')
"""
Things to remember:

- enumerate provides concise syntax for looping over an iterator and getting the
index of each item from the iterator as you go.

- Prefer enumerate instead of looping over a range and indexing into a sequence

- You can supply a second parameter to enumerate to specify the number from
which to begin counting (zero is the default)
"""
