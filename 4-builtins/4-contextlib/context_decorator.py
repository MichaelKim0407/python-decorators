import os

from contextlib import ContextDecorator

__author__ = 'Michael'


def getcwd_abs():
    return os.path.abspath(os.getcwd())


class CD(ContextDecorator):
    def __init__(self, path):
        self.original = getcwd_abs()
        self.path = os.path.abspath(path)

    def __enter__(self):
        os.chdir(self.path)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.original)


@CD('..')
def list_dir(path='.'):
    print(getcwd_abs())
    print(os.listdir(path))


if __name__ == '__main__':
    with CD('..'):
        print(getcwd_abs())
        print(os.listdir('.'))

    list_dir()
