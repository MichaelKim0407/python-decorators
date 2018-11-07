# Built-ins and libraries

## @dataclasses.dataclass

The [dataclasses](https://docs.python.org/3/library/dataclasses.html) module
is a new addition in Python 3.7 that utilizes
the [type annotation syntax](https://www.python.org/dev/peps/pep-0526/) introduced in 3.6
to create fully-functional classes that are used to store data.

Some consider dataclass to be an upgrade from
[`namedtuple`](https://docs.python.org/3/library/collections.html#collections.namedtuple).

In short, the decorator will read the type annotations
and create methods like `__init__`, `__repr__`, `__eq__`, etc.

* Example 1

    _(Script available)_

    ```python
    from dataclasses import dataclass

    @dataclass()
    class Vector2(object):
        x: float
        y: float = 0

        def __add__(self, other):
            return Vector2(self.x + other.x, self.y + other.y)

    if __name__ == '__main__':
        help(Vector2)

        v1 = Vector2(x=1)
        print(v1)
        v2 = Vector2(1, 0)
        print(v2)
        print(v1 == v2)

        v1.y = 3
        print(v1 + v2)
    ```

    It is worth noting that type annotations will not enforce variable types,
    and dataclass has no special logic regarding this either.
    To enforce variable types please see next example.

* Example 2

    _(Script available)_

    ```python
    import sys

    from dataclasses import dataclass

    def enforce_types(data_cls):
        __setattr = data_cls.__setattr__

        def __setattr__(self, key, value):
            if key in self.__class__.__dataclass_fields__:
                value = self.__dataclass_fields__[key].type(value)
            return __setattr(self, key, value)

        data_cls.__setattr__ = __setattr__

        return data_cls

    def math_dataclass(data_cls):
        def get_method(name):
            def __method(self, other):
                return self.__class__(**{
                    field_name: getattr(field.type, name)(
                        getattr(self, field_name),
                        getattr(other, field_name),
                    )
                    for field_name, field in self.__class__.__dataclass_fields__.items()
                })

            return __method

        for name in ['__add__', '__sub__', '__mul__', '__truediv__']:
            if hasattr(data_cls, name):
                continue
            setattr(data_cls, name, get_method(name))

        return data_cls

    class OperationNotAllowed(Exception):
        pass

    @math_dataclass
    @enforce_types
    @dataclass
    class Vector2(object):
        x: float
        y: float

        def __mul__(self, other):
            return self.x * other.x + self.y * other.y

        def __truediv__(self, other):
            raise OperationNotAllowed

    if __name__ == '__main__':
        v1 = Vector2(1, 2)
        print(v1)
        v1.x = 0
        print(v1)

        v2 = Vector2(1.5, 2.5)
        print(v1 + v2)
        print(v1 * v2)
        try:
            print(v1 / v2)
        except Exception as e:
            print(repr(e), file=sys.stderr)
    ```

[Prev](../4-contextlib/README.md) /
[Up](../README.md) /
[Next](../../5-why/README.md)
