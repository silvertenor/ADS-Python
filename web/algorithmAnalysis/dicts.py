# access elements by key, not position

# get item and set item are O(1)! (can sometimes degenerate to O(N))
# 'contains' also O(1)! (can sometimes degenerate)


import timeit
import random

print(f"{'n':10s}{'list':>10s}{'dict':>10s}")

for i in range(10000, 1_000_001, 20_000):
    t = timeit.Timer(f'random.randrange({i}) in x', 'from __main__ import random, x')
    x = list(range(i))
    lstTime = t.timeit(number=1000)
    x = {j: None for j in range(i)}
    dictTime = t.timeit(number=1000)

    print(f"{i:<10,}{lstTime:>10.3f}{dictTime:>10.3f}")


