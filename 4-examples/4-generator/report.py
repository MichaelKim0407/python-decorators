import functools

from util import read_lines

__author__ = 'Michael'


def report(log=print, name=None, interval=1000):
    """
    Report progress of a generator
    """

    def __decor(gen):
        _name = name or gen.__name__

        @functools.wraps(gen)
        def __new_func(*args, **kwargs):
            count = 0
            for item in gen(*args, **kwargs):
                yield item
                count += 1
                if count % interval == 0:
                    log("{}: yielded {} entries".format(_name, count))
            log("{}: finished with {} entries".format(_name, count))

        return __new_func

    return __decor


@report()
def read(path):
    for line in read_lines(path):
        if line.startswith('#'):
            continue
        yield line


if __name__ == '__main__':
    print(len(tuple(read('long.txt'))))
