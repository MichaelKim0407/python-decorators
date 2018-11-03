import math

__author__ = 'Michael'


class Vector2(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    @property
    def array(self):
        return self.x, self.y

    @array.setter
    def array(self, val):
        self.x, self.y = val

    @property
    def length(self):
        return math.sqrt(sum(i ** 2 for i in self.array))

    @length.setter
    def length(self, val):
        ratio = val / self.length
        self.x *= ratio
        self.y *= ratio

    @length.deleter
    def length(self):
        self.x = 0
        self.y = 0


if __name__ == '__main__':
    v = Vector2(1, 3)
    print(v.array)
    v.array = 2, 2
    print(v)

    print(v.length)
    v.length += math.sqrt(2)
    print(v)

    del v.length
    print(v)
