# Built-ins and libraries

* @property

    [`@property`](https://docs.python.org/3/library/functions.html#property)
    is a built-in decorator that transforms instance methods into properties.

    In practice properties are used just like value attributes -
    they can be accessed with dotted name without parentheses.

    (Executable scripts available in <a href="https://github.com/MichaelKim0407/python-decorators/tree/master/5-builtins/1-property" target="_blank">repo</a>.)

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

    For a property, the setter or deleter don't have to be defined,
    so you may create read-only properties.

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

[Prev](../README.md) /
[Up](../README.md) /
[Next](../2-functools/README.md)
