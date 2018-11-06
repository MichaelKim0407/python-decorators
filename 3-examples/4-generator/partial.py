import functools
from typing import Union, Type

from util import read_lines

__author__ = 'Michael'


def partial(
        empty_error: Union[bool, Type[Exception]] = False
):
    """
    Decorates a generator so that when called,
    it's partially executed until the first `yield` statement.

    If the result is empty (i.e. a `yield` statement is never reached),
    0. The generator will be fully executed; and
    1. If `empty_error` is False (default), an empty tuple will be returned; otherwise
    2. If `empty_error` is True, a StopIteration will be raised; otherwise
    3. `empty_error()` will be raised
    """

    def __decor(gen):
        @functools.wraps(gen)
        def __new_func(*args, **kwargs):
            iterator = gen(*args, **kwargs)
            try:
                first = next(iterator)
            except StopIteration:
                if not empty_error:
                    return ()
                elif isinstance(empty_error, bool):
                    # empty_error = True
                    raise
                else:
                    raise empty_error() from None

            def __new_generator():
                yield first
                for item in iterator:
                    yield item

            return __new_generator()

        return __new_func

    return __decor


class Float(Exception):
    pass


@partial()
def read_int(path):
    for line in read_lines(path):
        if line.startswith('#'):
            if 'float' in line:
                raise Float
            continue
        try:
            yield int(line)
        except ValueError:
            continue


def read_float(path):
    for line in read_lines(path):
        if line.startswith('#'):
            continue
        try:
            yield float(line)
        except ValueError:
            continue


def read(path):
    try:
        return read_int(path)
    except Float:
        return read_float(path)


if __name__ == '__main__':
    print(sum(read('numbers.txt')))
    # run without `@partial()`: will result in error
