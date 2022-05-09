"""
16. Prefer get over in and KeyError to Handle Missing dictionary keys
"""

counters = {
    'pumpernickel': 2,
    'sourdough': 1,
}

key = 'wheat'

if key in counters:
    count = counters[key]
else:
    count = 0

counters[key] = count + 1

try:
    count = counters[key]
except:
    count = 0

counters[key] = count + 1

count = counters.get(key, 0)
counters[key] = count + 1

# USING LISTS
votes = {
    'baguette': ['Bob', 'Alice'],
    'ciabatta': ['Coco', 'Deb'],
}

key = 'brioche'
who = 'Elmer'

if key in votes:
    names = votes[key]
else:
    votes[key] = names = []

names.append(who)
print(votes)

if (names := votes.get(key)) is None:
    votes[key] = names = []

names.append(who)

names = votes.setdefault(key, [])
names.append(who)


data = {}
key = 'foo'
value = []

data.setdefault(key, value)
print('Before', data)
value.append('hello')
print('After', data)

"""
Things to remember:

- There are four common ways to detect and handle missing keys in dictionaries:
using in expressions, KeyError exceptions, the get method, and the setdefault
method.

- The get method is best for dictionaries that contain basic types like,
counters, and is preferable along with assignment expressions when creating
dictionary values has a high cost or may raise exceptions.

- When the setdefault method of dict seems like the best fit for your problem,
you should consider using defaultdict instead.
"""
