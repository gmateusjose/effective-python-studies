"""
15. Be cautious when relying on dict insertion ordering
"""

baby_names = {
    'cat': 'kitten',
    'dog': 'puppy',
}
print(baby_names)

def my_func(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')

my_func(goose='gosling', kangaroo='joey')

class MyClass:
    def __init__(self):
        self.alligator = 'hatchling'
        self.elephant = 'calf'


a = MyClass()

for key, value in a.__dict__.items():
    print(f'{key} = {value}')

votes = {
    'otter': 1281,
    'polar bear': 587,
    'fox': 863,
}


def populate_ranks(votes, ranks):
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)

    for i, name in enumerate(names, 1):
        ranks[name] = i


def get_winner(ranks):
    return next(iter(ranks))


ranks = {}
populate_ranks(votes, ranks)
print(ranks)
winner = get_winner(ranks)
print(winner)


from collections.abc import MutableMapping


# class SortedDict(MutableMapping):
#     def __init__(self):
#         self.data = {}

#     def __getitem__(self, key):
#         return self.data[key]

#     def __setitem__(self, key, value):
#         self.data[key] = value

#     def __delitem__(self, key):
#         del self.data[key]

#     def __iter__(self):
#         keys = list(self.data.keys())
#         keys.sort()
#         for key in keys:
#             yield key

#     def __len__(self):
#         return len(self.data)


from typing import Dict, MutableMapping

def populate_ranks(votes: Dict[str, int], ranks: Dict[str, int]) -> None:
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i

def get_winner(ranks: Dict[str, int]) -> str:
    return next(iter(ranks))


class SortedDict(MutableMapping[str, int]):
    pass


sorted_ranks = SortedDict()
populate_ranks(votes, sorted_ranks)
print(sorted_ranks.data)
winner = get_winner(sorted_ranks)
print(winner)

"""
Things to remember:

- Since Python 3.y you can rely on the fact that iterating a dict instance's
contents will occur in the same order in which the keys were initially added.

- Python makes it easy to define objects that act like dictionaries but that
arent dict instances. For these types, you can't assume that insertion ordering
will be preserved

- There are three ways to be careful about dictionary-like classes:
    - Write code that doesn't rely on insertion ordering
    - Explicitly check for the dict type at runtime
    - Require dict values using type annotations and static analysis.
"""
