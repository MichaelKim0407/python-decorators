from functools import total_ordering

__author__ = 'Michael'


@total_ordering
class Integer(object):
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return self.x == other.x

    def __lt__(self, other):
        return self.x < other.x


if __name__ == '__main__':
    print(Integer(1) >= Integer(2))  # try removing @total_ordering decorator
