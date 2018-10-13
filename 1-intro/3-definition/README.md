# What is a Python decorator?

Another place where the decorator syntax is mentioned is the [function definitions](https://docs.python.org/3/reference/compound_stmts.html#function).

> A function definition may be wrapped by one or more [decorator](https://docs.python.org/3/glossary.html#term-decorator) expressions.
> Decorator expressions are evaluated when the function is defined, in the scope that contains the function definition.
> The result must be a callable, which is invoked with the function object as the only argument.
> The returned value is bound to the function name instead of the function object.
> Multiple decorators are applied in nested fashion.
> For example, the following code
>
>     @f1(arg)
>     @f2
>     def func(): pass
>
> is roughly equivalent to
>
>     def func(): pass
>     func = f1(arg)(f2(func))
>
> except that the original function is not temporarily bound to the name `func`.

Essentially it says the same as the glossary entry,
and a decorator is considered part of the function definition.

Similar text can also be found in the [class definitions](https://docs.python.org/3/reference/compound_stmts.html#class).

[Prev](../2-glossary/README.md) `|` [Top](../../README.md) > [What is a Python decorator?](../README.md) > Function definitions
