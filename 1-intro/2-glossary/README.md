# What is a Python decorator?

## Glossary

In the [glossary](https://docs.python.org/3/glossary.html#term-decorator) page there is an entry for the term decorator:

> A function returning another function, usually applied as a function transformation using the `@wrapper` syntax.
> Common examples for decorators are [`classmethod()`](https://docs.python.org/3/library/functions.html#classmethod) and [`staticmethod()`](https://docs.python.org/3/library/functions.html#staticmethod).
>
> The decorator syntax is merely syntactic sugar, the following two function definitions are semantically equivalent:
>
>     def f(...):
>         ...
>     f = staticmethod(f)
>
>     @staticmethod
>     def f(...):
>         ...
>
> The same concept exists for classes, but is less commonly used there.
> See the documentation for [function definitions](https://docs.python.org/3/reference/compound_stmts.html#function) and [class definitions](https://docs.python.org/3/reference/compound_stmts.html#class) for more about decorators.

However, it is rather incorrect in the sense that decorators can be much more than this,
and this piece of text has not changed since the Glossary page was added back in 2.6,
with the exception that it now mentions classes.

We can also see that the writers of the Python docs treat decorator as a syntactic sugar,
which explains why it is not extensively introduced.

[Prev](../1-pep-318/README.md) /
[Up](../README.md) /
[Next](../3-definition/README.md)
