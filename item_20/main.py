"""
20. Prefer raising exceptions to returning None
"""

def careful_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

x, y = 1, 0
result = careful_divide(x, y)
if result is None:
    print('Invalid inputs')

x, y = 0, 5
result = careful_divide(x, y)
if not result:
    print('Invalid inputs')  # This runs! But shouldn't


def careful_divide(a, b):
    try:
        return True, a/b
    except ZeroDivisionError:
        return False, None

success, result = careful_divide(x, y)
if not success:
    print('Invalid inputs')

x, y = 0, 5
_, result = careful_divide(x, y)
if not result:
    print('Invalid inputs')


def careful_divide(a, b):
    try:
        return a/b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs')

x, y = 5, 2
try:
    result = careful_divide(x, y)
except ValueError:
    print('Invalid inputs')
else:
    print('Result is %.1f' % result)


def careful_divide(a: float, b: float) -> float:
    """
    Divides a by b.

    Raises:
        ValueError: When the inputs cannot be divided.
    """
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs')


"""
Things to remember:

- Functions that return None to indicate special meaning are error prone because
None and other values (e.g. zero, the empty string) all evaluate to False in
conditional expressions.

- Raise exceptions to indicate special situations instead of returning None.
Expect the calling code to handle exceptions properly when they're documented.

- Type annotations can be used to make it clear that a function will never
return the value None, even in special situations.
"""
