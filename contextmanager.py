import time
from contextlib import contextmanager

@contextmanager
def timeit(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"{label}: {end - start:.4f} seconds")

with timeit("Example Timing"):
    total = 0
    for i in range(1000000):
        total += i


@contextmanager
def list_transaction(lst):
    working = list(lst)
    yield working
    lst[:] = working

items = [1, 2, 3]
with list_transaction(items) as workin:
    workin.append(4)
    workin.append(5)

print(items)

try: 
    with list_transaction(items) as workin:
        workin.append(6)
        workin.append(7)
        raise RuntimeError("Simulated error")
except RuntimeError as e:
    print(f"Error occurred: {e}")
# This will not change the original list due to the error
print(items)  # Output: [1, 2, 3, 4, 5]
