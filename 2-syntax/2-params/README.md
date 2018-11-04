# A dive into the syntax

## Passing parameters

The syntax is a little bit different if we wish to pass parameters to a decorator:

    def with_params(...):
        def __decor(func):
            ...

        return __decor

The decorator will first take its parameters,
and then make another call to the decorated function.

    @with_params(0)
    def my_func():
        pass

is the equivalent of

    my_func = with_params(0)(my_func)

[Prev](../1-write/README.md) /
[Up](../README.md) /
[Next](../3-understand/README.md)
