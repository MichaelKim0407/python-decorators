# Examples

## Annotation

Before we use a decorator to do something, we can instead use it to do nothing.

    def annotate(*args, **kwargs):
        def __decor(func):
            return func

        return __decor

This will allow us to use the decorator to write comment-like annotations,
only that they are much easier to search for than comments
when using an IDE or regex.

    @annotate(endpoint='/', name='index')
    def index():
        return "Hello, world!"

It can be later improved upon,
as we can at any time rewrite it into a functional decorator.

[Prev](../README.md) /
[Up](../README.md) /
[Next](../2-register/README.md)
