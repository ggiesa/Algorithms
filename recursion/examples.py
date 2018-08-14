from time import time

# Cache
mem = {}

class Memoize:
    def __init__(self, func):
        self.func = func
        self.memo = {}

    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.func(*args)
        return self.memo[args]


def memoize(f):
    cache = {}
    def mem(*args, **kargs):
        if not args in cache:
            cache[args] = f(*args)
        return cache[args]
    return mem


def factorial(n):
    '''Basic example, no memoization'''
    # Base case:
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def factorial_mem(n):
    '''Basic example, memoization with global cache'''
    if n < 2:
        return 1
    elif n not in mem:
        mem[n] = n*factorial_mem(n-1)

    return mem[n]

@memoize
def factorial_dec(n):
    '''Memoization done with function decorator.'''
    # Base case:
    if n == 0:
        return 1
    else:
        return n*factorial_dec(n-1)

@Memoize
def factorial_cls(n):
    '''Memoization done with class decorator.'''
    # Base case:
    if n == 0:
        return 1
    else:
        return n*factorial_cls(n-1)


def timer(msg, function):
    t = time()
    for i in range(500):
        _ = function(i)
    print(msg, time()-t)

check = {
    'Unmemoized':factorial,
    'Memoized':factorial_mem,
    'Memoized with function':factorial_dec,
    'Memoized with class':factorial_cls,
}
for msg, function in check.items():
    timer(msg, function)
