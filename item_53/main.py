"""
53. Use threads for blocking I/O, avoid for parallelism
"""
# FIRST EXAMPLE
import time


def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i

numbers = [2139079, 1214759, 1516637, 1852285]
start = time.time()

for number in numbers:
    list(factorize(number))

end = time.time()
delta = end - start
print(f'Took {delta:.3f} seconds')

# SECOND EXAMPLE
from threading import Thread

class FactorizeThread(Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        self.factors = list(factorize(self.number))

start = time.time()

threads = []
for number in numbers:
    thread = FactorizeThread(number)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

end = time.time()
delta = end - start
print(f'Took {delta:.3f} seconds')

# THIRD EXAMPLE
import select
import socket

def slow_systemcall():
    select.select([socket.socket()], [], [], 0.1)

start = time.time()

for _ in range(5):
    slow_systemcall()

end = time.time()
delta = end - start
print(f'Took {delta:.3f} seconds')

# FOURTH EXAMPLE
start = time.time()
threads = []
for _ in range(5):
    thread = Thread(target=slow_systemcall)
    thread.start()
    threads.append(thread)

def compute_helicopter_location(index):
    print(f'helicopter {index} location')

for i in range(5):
    compute_helicopter_location(i)

for thread in threads:
    thread.join()

end = time.time()
delta = end - start
print(f'Took {delta:.3f} seconds')

"""
Things to remember:

- Python threads can't run in parallel on multiple CPU cores because of the
global interpreter lock (GIL)

- Python threads are still useful despite the GIL because they provide an easy
way to do multiple things seemingly at the same time.

- Use Python threads to make multiple system calls in parallel. This allows you
to do blocking I/O at the same time as computation
"""
