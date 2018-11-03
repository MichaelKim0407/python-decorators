import time

import functools

__author__ = 'Michael'


def timed(func):
    @functools.wraps(func)
    def __new_func(*args, **kwargs):
        start = time.time()
        try:
            return func(*args, **kwargs)
        finally:
            end = time.time()
            print(f"{func.__name__} took {end - start} seconds")

    return __new_func


@timed
def f(x):
    for i in range(10 ** x):
        pass


if __name__ == '__main__':
    f(5)
    f(6)
    f(7)
    f(8)
