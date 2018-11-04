# Built-ins and libraries

## @property and @cached_property

* @property

    [`@property`](https://docs.python.org/3/library/functions.html#property)
    is a built-in decorator that transforms instance methods into properties.

    In practice properties are used just like value attributes -
    they can be accessed with dotted name without parentheses.

    (Executable scripts available in [repo](https://github.com/MichaelKim0407/python-decorators/tree/master/5-builtins/1-property).)

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

* @cached_property

    `@cached_property` is available in both the
    [cached-property](https://github.com/pydanny/cached-property) package
    and the [Django](https://docs.djangoproject.com/en/2.1/ref/utils/#django.utils.functional.cached_property) package.

    Instead of being a property with setter and deleter,
    it is just a getter that evaluates and replaces it self with the result
    when it is first accessed.

    It is most useful in two cases:

    1. There is a resource-heavy calculation that should only be done on demand.

    2. A calculated value that does not change while changes are made to the class instance.

    Especially when both are true.

        import sys
        import time

        from cached_property import cached_property

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

[Prev](../README.md) /
[Up](../README.md) /
[Next](../2-functools/README.md)
