# Your code here
import math
import random


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    print('1', v)
    v = math.factorial(v)
    print('2', v)
    v //= (x + y)
    print('3', v)
    v %= 982451653

    return v

# print('slowfun_too_slow', slowfun_too_slow(2, 4))



def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    cache = {}
    key  = (x,y)
    if key not in cache:
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653
        cache[key] = v
    return cache[key]

# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
