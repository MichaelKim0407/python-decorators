import sys

from dataclasses import dataclass

__author__ = 'Michael'


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
