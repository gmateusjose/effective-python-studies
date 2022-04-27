"""
08. Use zip to process Iterators in Parallel
"""

names = ['Cecilia', 'Lise', 'Marie']
counts = [len(n) for n in names]
print(counts)

longest_name = None
max_count = 0

for i in range(len(names)):
    count = counts[i]
    if count > max_count:
        longest_name = names[i]
        max_count = count

print(longest_name)

for i, name in enumerate(names):
    count = counts[i]
    if count > max_count:
        longest_name = name
        max_count = count

print(longest_name)

for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_count = count

names.append('Rosalind')
for name, count in zip(names, counts):
    print(name)

import itertools
for name, count in itertools.zip_longest(names, counts):
    print(f'{name}: {count}')

"""
Things to remember:

- The zip built-in function can be used to iterate over multiple iterators in
parallel.

- zip creates a lazy generator that produces tuples, so it can be used on
infinitely long inputs

- zip truncates its output silently to the shortest iterator if you supply it
with iterators of different lengths.

- Use the zip_longest function from the itertools built-in module if you want to
use zip on iterators of unequal lengths without truncation.
"""
