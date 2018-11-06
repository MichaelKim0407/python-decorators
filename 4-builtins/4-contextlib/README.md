# Built-ins and libraries

## contextlib

The [contextlib](https://docs.python.org/3/library/contextlib.html) module
allows easy creation of context managers to be used in `with` clauses.

* contextmanager

    [Doc](https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager):

    > This function is a [decorator](https://docs.python.org/3/glossary.html#term-decorator)
    > that can be used to define a factory function for
    > [with](https://docs.python.org/3/reference/compound_stmts.html#with)
    > statement context managers,
    > without needing to create a class or separate
    > [`__enter__()`](https://docs.python.org/3/reference/datamodel.html#object.__enter__) and
    > [`__exit__()`](https://docs.python.org/3/reference/datamodel.html#object.__exit__) methods.

    It needs to be used with a specific syntax:

    ```python
    try:
        yield ...  # value
    finally:
        ...  # exit
    ```

    _(Script available)_

    ```python
    import os

    from contextlib import contextmanager

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
    ```

    There is also [@asynccontextmanager](https://docs.python.org/3/library/contextlib.html#contextlib.asynccontextmanager) for `async with`.

* ContextDecorator

    [Doc](https://docs.python.org/3/library/contextlib.html#contextlib.ContextDecorator):

    > A base class that enables a context manager to also be used as a decorator.
    >
    > Context managers inheriting from `ContextDecorator` have to implement `__enter__` and `__exit__` as normal.
    > `__exit__` retains its optional exception handling even when used as a decorator.

    _(Script available)_

    ```python
    import os

    from contextlib import ContextDecorator

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
    ```

[Prev](../3-functools/README.md) /
[Up](../README.md) /
[Next](../5-dataclass/README.md)
