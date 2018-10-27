# What is a Python decorator?

In Python's [full grammer specification](https://docs.python.org/3/reference/grammar.html?highlight=decorator) this part can be found:

>     decorator: '@' dotted_name [ '(' [arglist] ')' ] NEWLINE
>     decorators: decorator+
>     decorated: decorators (classdef | funcdef | async_funcdef)

This is basically saying,
decorators start with an `@`,
can optionally have parameters,
must be in a line by itself,
and we can stack one or several decorators before a class or function definition.

[Prev](../3-definition/README.md) /
[Up](../README.md) /
[Next](../../2-syntax/README.md)
