"""
12. Avoid striding and slicing in a single expression
"""

x = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = x[::2]
evens = x[1::2]

print(odds)
print(evens)


x = b'mongoose'
y = x[::-1]
print(y)

w = 'uau'
x = w.encode('utf-8')
y = x[::-1]
z = y.decode('utf-8')

"""
Things to remember:

- Specifying start, end, and stride in a slice can be extremely confusing.

- Prefer using positive stride values in slices without start or end indexes.
Avoid negative stride values if possible.

- Avoid using start, end, and stride together in a single slice. If you need all
three parameters, consider doing two assignments (one to stride and another to
slice) or using islice from the itertools built-in module.

"""
