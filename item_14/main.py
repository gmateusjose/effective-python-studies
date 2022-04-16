"""
14. Sort by complex criteria using the key parameter
"""

# FIRST EXAMPLE
numbers = [93, 86, 11, 68, 70]
numbers.sort()
print(numbers)


# SECOND EXAMPLE
class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f"Tool({self.name!r}, {self.weight})"


tools = [
    Tool('level', 3.5),
    Tool('hammer', 1.25),
    Tool('screwdriver', 0.5),
    Tool('chisel', 0.25)
]

print('\nUnsorted: ', repr(tools))

tools.sort(key=lambda x: x.name)
print('Sorted: ', tools)

tools.sort(key=lambda x: x.weight)
print('By weight: ', tools)


# THIRD EXAMPLE
places = ['home', 'work', 'New York', 'Paris']
places.sort()
print('\nCase sensitive: ', places)

places.sort(key=lambda x: x.lower())
print('Case insensitive: ', places)


# FOURTH EXAMPLE
power_tools = [
    Tool('drill', 4),
    Tool('circular saw', 5),
    Tool('jackhammer', 40),
    Tool('sander', 4),
]

power_tools.sort(key=lambda x: (x.weight, x.name))
print(power_tools)

power_tools.sort(key=lambda x: x.name)
power_tools.sort(key=lambda x: x.weight, reverse=True)
print(power_tools)

"""
Things ro remember:

- The sort method of the list type can be used to rearrange a list's contents by
the natural ordering of built-in types like strings, integers, tuples and so on.

- The sort method doesn't work for objects unless they define a natural ordering
using special methods, which is uncommon.

- The key parameter of the sort method can be used to supply a helper function
that returns the value to use for sorting in place of each item from the list.

- Returning a tuple from the key function allows you to combine multiple sorting
criteria together. The unary minus operator can be used to reverse individual
sort orders for types that allow it.

- For types that can't be negated, you can combine many sorting criteria
together by calling the sort method multiple times using diferent key functions
and reverse values, in the order of lowest rank sort call to highest rank sort
call.
"""
