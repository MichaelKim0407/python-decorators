import functools

from util import read_lines

__author__ = 'Michael'


def execute(type=tuple):
    """
    Execute a generator and store results in a storage (default is tuple)
    """

    def __decor(gen):
        @functools.wraps(gen)
        def __new_func(*args, **kwargs):
            return type(gen(*args, **kwargs))

        return __new_func

    return __decor


@execute()
def read_all(path):
    for line in read_lines(path):
        if line.startswith('#'):
            continue
        yield line


if __name__ == '__main__':
    print(read_all('numbers.txt'))
