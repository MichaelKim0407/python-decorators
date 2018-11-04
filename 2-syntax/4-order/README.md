# A dive into the syntax

## Orders do matter

When multiple decorators are applied, the order of them does matter.

    @a
    @b
    def f():
        pass

would mean

    f = a(b(f))

whereas

    @b
    @a
    def f():
        pass

would mean

    f = b(a(f))

Sometimes the end results would be interchangeable,
but there are also cases where decorators must be applied in a specific order,
so it is important to remember that they are different.

[Prev](../3-understand/README.md) /
[Up](../README.md) /
[Next](../../3-examples/README.md)
