import sys
import time

try:
    from cached_property import cached_property
except ImportError:
    print('Please install cached-property:\n\tpip install cached-property', file=sys.stderr)
    raise

__author__ = 'Michael'


class C(object):
    def __init__(self, x):
        self.__x = x

    @property
    def x(self):
        return self.__x

    @cached_property
    def squared(self):
        print('Calculating...', file=sys.stderr)
        time.sleep(1)
        return self.x ** 2


if __name__ == '__main__':
    c = C(10)
    print(c.squared)
    print(c.squared)
