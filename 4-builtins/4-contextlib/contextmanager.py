import os

from contextlib import contextmanager

__author__ = 'Michael'


def getcwd_abs():
    return os.path.abspath(os.getcwd())


@contextmanager
def cd(path):
    cwd = getcwd_abs()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(cwd)


if __name__ == '__main__':
    print(getcwd_abs())
    with cd('..'):
        print(getcwd_abs())
    print(getcwd_abs())
