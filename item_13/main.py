"""
13. Prefer Catch-all Unpacking over slicing
"""

car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
car_ages_descending = sorted(car_ages, reverse=True)

oldest, second_oldest, *others = car_ages_descending
print(oldest, second_oldest, others)

oldest, *others, youngest = car_ages_descending
print(oldest, youngest, others)

*others, second_youngest, youngest = car_ages_descending
print(youngest, second_youngest, others)


short_list = [1, 2]
first, second, *rest = short_list
print(first, second, rest)


it = iter(range(1, 3))
first, second = it
print(f'{first} and {second}')


def generate_csv():
    yield ('Date', 'Make', 'Model', 'Year', 'Price')

all_csv_rows = list(generate_csv())
header = all_csv_rows[0]
rows = all_csv_rows[1:]
print('CSV Header:', header)
print('Row Count:', len(rows))

it = generate_csv()
header, *rows = it
print('CSV Header:', header)
print('Row Count:', len(rows))

"""
Things to remember:

- Unpacking assignments may use a starred expression to catch all values that
weren't assigned to the other parts of the unpacking pattern into a list.

- Starred expressions may appear in any position, and they will always become a
list containing the zero or more values they receive.

- When dividing a list into non-overlapping pieces, catch-all unpacking is much
less error prone than slicing and indexing.
"""
