from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n -1) + fib(n-2)

result = [fib(n) for n in range(16)]

print(result)

print(fib.cache_info())
