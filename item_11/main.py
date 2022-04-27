"""
11. Know how to slice sequences
"""

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('Middle two', a[3: 5])
print('All but ends', a[1:7])

assert a[:5] == a[0:5]
assert a[5:] == a[5:len(a)]

first_twenty_items = a[:20]
last_twenty_items = a[-20:]

try:
    print(f'{a[20]}')
except IndexError:
    print('index error raised')

b = a[3:]
print('Before: ', b)

b[1] = 99
print('After:     ', b)
print('No change: ', a)

print('Before:    ', a)
a[2:7] = [99, 22, 14]
print('After:     ', a)

print('Before:    ', a)
a[2:3] = [47, 11]
print('After:     ', a)

b = a[:]
assert b == a and b is not a

b = a
print('Before a', a)
print('Before b', b)

a[:] = [101, 102, 103]
assert a is b

print('After a', a)
print('After b', b)

"""
Things to remember:

- Avoid being verbose when slicing: Don't supply 0 for the start index or the
length of the sequence for the end index

- Slicing is forgiving of start or end indexes are out of bounds, which means
it's easy to express slices on the front or back boundaries of a sequence
(like a[:20] or a[-20:])

- Assigning to a list slice replaces that range in the original sequence with
what's referenced even if the lengths are different.
"""
