__author__ = 'Michael'


class C(object):
    def __init__(self, x):
        self.__private = x

    @property
    def x(self):
        return self.__private


if __name__ == '__main__':
    c = C(1)
    print(c.x)

    try:
        print(c.__private)
    except AttributeError as e:
        print(repr(e))

    try:
        c.x = 2
    except AttributeError as e:
        print(repr(e))
