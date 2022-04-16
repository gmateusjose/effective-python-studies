"""
21. Know how closures interact with variable scope
"""

# FIRST EXAMPLE
def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)

    values.sort(key=helper)

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)


# SECOND EXAMPLE
def sort_priority2(numbers, group):
    found = False

    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found

found = sort_priority2(numbers, group)
print('Found: ', found)
print(numbers)


# THIRD EXAMPLE
class Sorter:
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)


sorter = Sorter(group)
numbers.sort(key=sorter)
assert sorter.found is True

"""
Things to remember:

- Closure functions can refer to variables from any of the scopes in which they
were defined.

- By default, closures can't affect enclosing scopes by assigning variables

- Use the nonlocal statement to indicate when a closure can modify a variable
in its enclosing scopes.

- Avoid using nonlocal statements for anything beyond simple functions.
"""
