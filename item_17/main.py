"""
17. Prefer defaultdict over setdefault to handle missing items in internal state
"""

visits = {
    'Mexico': {'Tulum', 'Puerto Vallarta'},
    'Japan': {'Hakone'},
}

visits.setdefault('France', set()).add('Arles')

if (japan := visits.get('Japan')) is None:
    visits['Japan'] = japan = set()
japan.add('Kyoto')

print(visits)


class Visits:
    def __init__(self):
        self.data = {}

    def add(self, country, city):
        city_set = self.data.setdefault(country, set())
        city_set.add(city)


visits = Visits()
visits.add('Russia', 'Yekaterinburg')
visits.add('Tanzania', 'Zanzibar')
print(visits.data)


from collections import defaultdict

class Visits:
    def __init__(self):
        self.data = defaultdict(set)

    def add(self, country, city):
        self.data[country].add(city)

visits = Visits()
visits.add('England', 'Bath')
visits.add('England', 'London')
print(visits.data)

"""
Things to remember:

- If you're creating a dictionary to manage an arbitrary set of potential keys,
then you should prefer using a defaultdict instance from the collections built-in
module if it suits your problem

- If a dictionary of arbitrary keys is passed to you, and you don't control its
creation, then you should prefer the get method to access its items. However,
it's worth considering using the setdefault method fo the few situations in which
it leads to shorter code.
"""
