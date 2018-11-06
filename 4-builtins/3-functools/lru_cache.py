import sys
import time

from functools import lru_cache

__author__ = 'Michael'


@lru_cache()
def fibonacci(n):
    print(f"Calculating {n}", file=sys.stderr)
    time.sleep(0.1)
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(fibonacci(10))
    print(fibonacci(20))
