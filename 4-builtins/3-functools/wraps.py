from functools import wraps

__author__ = 'Michael'


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
