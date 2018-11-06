from dataclasses import dataclass

__author__ = 'Michael'


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
