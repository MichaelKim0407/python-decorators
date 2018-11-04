# A dive into the syntax

## A better understanding

One way to see decorator with parameters is that there simply isn't such a thing.

A decorator is exactly what follows `@` in the same line.

In our previous example, the decorator is not `with_params`,
but `with_params(0)`, which returns `__decor`,
so `__decor` is the actual decorator.

The interpreter doesn't care what you put after `@`, as long as the syntax is followed.
All it asks is a callable that can be called with one parameter.

Once we realize this, we can write decorators in a variety of ways:

    @clazz  # __init__
    ...

    @instace  # __call__
    ...

    @instance.method
    ...

In fact, it is a common practice to write "decorators with parameters" as classes:

    class with_params:  # PEP 8 freaks out
        def __init__(...[decorator parameters]):
            ...

        def __call__(decorated):
            ...

Unfortunately, as per the grammar specs,
a decorator can only come in the format of `dotted_name [ '(' [arglist] ')' ]`,
which means the following code will be `SyntaxError`, although they make perfect sense:

    @decorator_list[0]
    ...

    @some_func(...)(...)
    ...

However, we can circumvent this by using a function

    def as_is(x):
        return x

    @as_is(decorator_list[0])
    ...

which is kind of silly, to be honest.

But still, it's probably best to avoid writing like this.
In the spirit of being Pythonic, if there's something the interpreter doesn't like,
there's probably a better way to write it.

[Prev](../2-params/README.md) /
[Up](../README.md) /
[Next](../4-order/README.md)
