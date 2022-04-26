"""
05. Write helper functions instead of complex expressions
"""

# First Example
from urllib.parse import parse_qs

my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)

print(repr(my_values))
print('Red:     ', my_values.get('red'))
print('Green:   ', my_values.get('green'))
print('Opacity: ', my_values.get('opacity'))

red = my_values.get('red', [''])[0] or 0
green = my_values.get('green', [''])[0] or 0
opacity = my_values.get('opacity', [''])[0] or 0

print(f'Red:     {red!r}')
print(f'Green:   {green!r}')
print(f'Opacity: {opacity!r}')

green_str = my_values.get('green', [''])
if green_str[0]:
    green = int(green_str[0])
else:
    green = 0

def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        return int(found[0])
    return default

green = get_first_int(my_values, 'green')

"""
Things to remember:

- Python's syntax makes it easy to write single-line expressions that are overly
complicated and difficult to read.

- Move complex expressions into helper functions, especially if you need to use
the same logic repeatedly.

- An if/else expression provides a more readable alternative to using the
Boolean operators or and in expressions
"""
