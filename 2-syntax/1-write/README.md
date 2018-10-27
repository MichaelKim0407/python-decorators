# A dive into the syntax

Although we shouldn't take "a function that returns a function" as the definition,
it is still the simplest form of decorator:

    def hello_decorator(func):
        def __new_func(*args, **kwargs):
            # do stuff with `func`, `args` and `kwargs`
            ...

        return __new_func

This is rather straightforward. `hello_decorator` took a function as its argument,
and returned a modified version of it.

    @hello_decorator
    def my_func():
        pass

[Prev](../README.md) /
[Up](../README.md) /
[Next](../2-params/README.md)
