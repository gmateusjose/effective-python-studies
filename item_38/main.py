"""
38. Accept functions instead of classes for simple interfaces
"""

# FIRST EXAMPLE
names = ['Socrates', 'Archimedes', 'Plato', 'Aristotle']
names.sort(key=len)
print(names)


# SECOND EXAMPLE
def log_missing():
    print('Key added')
    return 0

from collections import defaultdict

current = {'green': 12, 'blue': 3}
increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9),
]

result = defaultdict(log_missing, current)
print('Before: ', dict(result))

for key, amount in increments:
    result[key] += amount

print('After: ', dict(result))


# THIRD EXAMPLE
def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count # Stateful closure
        added_count += 1
        return 0

    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount

    return result, added_count

result, count = increment_with_report(current, increments)
assert count == 2


# FOURTH EXAMPLE
class CountMissing:
    def __init__(self):
        self.added = 0

    def missing(self):
        self.added += 1
        return 0


counter = CountMissing()
result = defaultdict(counter.missing, current)
for key, amount in increments:
    result[key] += amount
assert counter.added == 2


# FIFTH EXAMPLE
class BetterCountMissing:
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0


counter = BetterCountMissing()
result = defaultdict(counter, current)
for key, amount in increments:
    result[key] += amount
assert counter.added == 2

"""
Things to remember:

- Instead of defining and instantiating classes, you can often simply use
functions for simple interfaces between components in Python.

- References to functions and methods in Python are first class, meaning they
can be used in expressions (like any other type).

- The __call__ special method enables instances of a class to be called like
plain Python functions.

- When you need a function to mantain state, consider defining a class that
provides the __call__ method instead of defining a stateful closure.
"""
