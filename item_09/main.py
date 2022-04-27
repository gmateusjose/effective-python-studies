"""
09. Avoid else blocks after for and while loops
"""

for i in range(3):
    print('Loop', i)
else:
    print('Else block!')


for i in range(3):
    print('Loop', i)
    if i == 1:
        break
else:
    print('Else block!')

for x in []:
    print('Never runs')
else:
    print('For Else block!')

while False:
    print('Never runs')
else:
    print('While Else block!')

a = 4
b = 9

for i in range(2, min(a, b) + 1):
    print('Testing', i)
    if a % i == 0 and b % i == 0:
        print('Not coprime')
        break
else:
    print('coprime')


def coprime(a, b):
    for i in range(2, min(a, b) + 1):
        if (a % i == 0) and (b % i == 0):
            return False
    return True

assert coprime(4, 9)
assert not coprime(3, 6)

"""
Things to remember:

- Python has special syntax that allow else blocks to immediately follow for and
while loop interior blocks.

- The else block after a loop runs only if the loop body did not encounter a
break statement

- Avoid using else blocks after loops because their behavior isn't intuitive and
can be confusing
"""
