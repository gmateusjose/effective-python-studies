"""
10. Prevent repetition with assignment expressions
"""

fresh_fruit = {
    'apple': 10,
    'banana': 8,
    'lemon': 5,
}

def make_lemonade(count):
    print(f'making lemonade with {count} lemons')

def out_of_stock():
    print('out of stock')

count = fresh_fruit.get('lemon', 0)
if count:
    make_lemonade(count)
else:
    out_of_stock()

if count := fresh_fruit.get('lemon', 0):
    make_lemonade(count)
else:
    out_of_stock()

def make_cider(count):
    print(f'making cider with {count} apples')

if (count := fresh_fruit.get('apple', 0)) >= 4:
    make_cider(count)
else:
    out_of_stock()

def slice_bananas(count):
    print(f'slicing {count} bananas')

class OutOfBananas(Exception):
    pass

def make_smoothies(count):
    print(f'making smoothies with {count} bananas')

pieces = 0
if (count := fresh_fruit.get('banana', 0)) >= 2:
    pieces = slice_bananas(count)

try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()

if (count := fresh_fruit.get('banana', 0)) >= 2:
    pieces = slice_bananas(count)
    to_enjoy = make_smoothies(pieces)
elif (count := fresh_fruit.get('apple', 0)) >= 4:
    to_enjoy = make_cider(count)
elif count := fresh_fruit.get('lemon', 0):
    to_enjoy = make_lemonade(count)
else:
    to_enjoy = 'Nothing'

"""
Things to remember:

- Assignment expressions use the walrus operator (:=) to both assign and
evaluate variable names in a single expression, thus reducing repetition.

- When an assignment expression is a subexpression of a larger expression, it
must be surrounded with parentheses

- Although switch/case statements and do/while loops are not available in Python,
their functionality can be emulated much more clearly by using assignment expressions.
"""
