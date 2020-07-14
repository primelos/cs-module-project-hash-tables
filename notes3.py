import math
#0,1,1,2,3,5,8,13,21,34

# Recursive functions
# base case - where to stop
# move towards the base case
# function has to call its self

def slow_fibonacci(n, total = 0):
    if n <= 1:
        return n
    
    return fibonacci(n-1) + fibonacci(n-2)

cache = {}
def fibonacci(n):
    if n <= 1:
        return n
    
    if n not in cache:
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
    
    return cache[n]

# use a cache
# memoizing
# dynamic programming

print(fibonacci(2))
print(fibonacci(100))

# _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
# _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
# _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+




# lookup_table = {} 

# def inverse_root(n):
#     return 1 / math.sqrt(n)


# def populate_lookup_table():
#     for i in range(1, 1000):
#         pass
    

# populate_lookup_table()
# print(populate_lookup_table[142])

