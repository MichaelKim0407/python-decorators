# Built-ins and libraries

## functools

The [functools](https://docs.python.org/3/library/functools.html) module
provides some useful tools for functions,
including several decorators.

(Executable scripts in [repo](https://github.com/MichaelKim0407/python-decorators/tree/master/4-builtins/3-functools).)

* @wraps

    [`@wraps`](https://docs.python.org/3/library/functools.html#functools.wraps)
    is useful when creating decorators.
    It updates the new function to "look like" the original function.

    ```python
    from functools import wraps

    def decorator(func):
        @wraps(func)
        def __new_func(*args, **kwargs):
            # do stuff
            return func(*args, **kwargs)

        return __new_func

    @decorator
    def f():
        """
        This is f!
        :return:
        """
        pass

    if __name__ == '__main__':
        help(f)  # try removing the @wraps decorator
    ```

* @lru_cache

    [`@lru_cache`](https://docs.python.org/3/library/functools.html#functools.lru_cache)
    lets a function memorize its previous calls and their results,
    eliminating the need to make repetitive calculations.

    ```python
    import sys
    import time

    from functools import lru_cache

    @lru_cache()
    def fibonacci(n):
        print("Calculating {}".format(n), file=sys.stderr)
        time.sleep(0.1)
        if n <= 0:
            return 0
        if n == 1:
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)

    if __name__ == '__main__':
        print(fibonacci(10))
        print(fibonacci(20))
    ```

    There is also the "lru" aspect of the tool,
    which has a more detailed explanation in the docs.

* @total_ordering

    [Doc](https://docs.python.org/3/library/functools.html#functools.total_ordering):

    > Given a class defining one or more rich comparison ordering methods,
    > this class decorator supplies the rest.
    > This simplifies the effort involved in specifying all of the possible rich comparison operations:
    >
    > The class must define one of [`__lt__()`](https://docs.python.org/3/reference/datamodel.html#object.__lt__),
    > [`__le__()`](https://docs.python.org/3/reference/datamodel.html#object.__le__),
    > [`__gt__()`](https://docs.python.org/3/reference/datamodel.html#object.__gt__),
    > or [`__ge__()`](https://docs.python.org/3/reference/datamodel.html#object.__ge__).
    > In addition, the class should supply an [`__eq__()`](https://docs.python.org/3/reference/datamodel.html#object.__eq__) method.

    ```python
    from functools import total_ordering

    @total_ordering
    class Integer(object):
        def __init__(self, x):
            self.x = x

        def __eq__(self, other):
            return self.x == other.x

        def __lt__(self, other):
            return self.x < other.x

    if __name__ == '__main__':
        print(Integer(1) >= Integer(2))  # try removing @total_ordering decorator
    ```

[Prev](../2-property/README.md) /
[Up](../README.md) /
[Next](../4-contextmanager/README.md)
