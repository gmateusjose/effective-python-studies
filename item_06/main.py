"""
06. Prefer Multiple assignment unpacking over indexing
"""

snack_calories = {'chips': 140, 'popcorn': 80, 'nuts': 190}
items = tuple(snack_calories.items())
print(items)

item = ('Peanut butter', 'Jelly')
first, second = item
print(first, 'and', second)

def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i-1]:
                a[i-1], a[i] = a[i], a[i-1]

names = ['pretzels', 'carrots', 'arugula', 'bacon']
bubble_sort(names)
print(names)

snacks = [('bacon', 350), ('donut', 240), ('muffin', 190)]
for rank, (name, calories) in enumerate(snacks, 1):
    print(f'#{rank}: {name} has {calories} calories')

"""
Things to remember:

- Python has special syntax called unpacking for assigning multiple values in a
single statement.

- Unpacking is generalized in Python and can be applied to any iterable, including
many levels of iterables within iterables.

- Reduce visual noise and increase code clarity by using unpacking to avoid
explicitly indexing into sequences.
"""
