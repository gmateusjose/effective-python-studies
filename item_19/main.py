"""
19. Never unpack more than three variables when functions return multiple values
"""

def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum

lengths = [63, 73, 72, 60, 67, 66, 71, 72, 70]
minimum, maximum = get_stats(lengths)
print(f'Min: {minimum}, Max: {maximum}\n')


def get_avg_ratio(numbers):
    average = sum(numbers) / len(numbers)
    scaled = [x / average for x in numbers]
    scaled.sort(reverse=True)
    return scaled

longest, *middle, shortest = get_avg_ratio(lengths)
print(f'Longest: {longest:>4.0%}')
print(f'Shortest: {shortest:>4.0%}\n')


def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    count = len(numbers)
    average = sum(numbers) / count

    sorted_numbers = sorted(numbers)
    middle = count // 2
    if count % 2 == 0:
        lower = sorted_numbers[middle-1]
        upper = sorted_numbers[middle]
        median = (lower + upper) / 2
    else:
        median = sorted_numbers[middle]
    
    return minimum, maximum, average, median, count

minimum, maximum, average, median, count = get_stats(lengths)
print(f'Min: {minimum}, Max: {maximum}')
print(f'Average: {average}, Median: {median}, Count {count}')

"""
Things to remember:

- You can have functions return multiple values by putting them in a tuple and
having the caller take advantage of Python's unpacking syntax.

- Multiple return values from a function can also be unpacked by catch-all
starred expressions.

- Unpacking into four or more variables is error prone and should be avoided;
instead, return a small class or namedtuple instance.
"""
