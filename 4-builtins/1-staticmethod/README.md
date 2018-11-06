# @staticmethod and @classmethod

* @staticmethod

    [Doc](https://docs.python.org/3/library/functions.html#staticmethod)

    > Transform a method into a static method.
    >
    > A static method does not receive an implicit first argument.
    > To declare a static method, use this idiom:
    >
    > ```python
    > class C:
    >     @staticmethod
    >     def f(arg1, arg2, ...): ...
    > ```
    >
    > The `@staticmethod` form is a function decorator –
    > see the description of function definitions in Function definitions for details.
    >
    > It can be called either on the class (such as `C.f()`) or on an instance (such as `C().f()`).
    > The instance is ignored except for its class.

* @classmethod

    [Doc](https://docs.python.org/3/library/functions.html#classmethod)

    > ```python
    > class C:
    >     @classmethod
    >     def f(cls, arg1, arg2, ...): ...
    > ```
    >
    > It can be called either on the class (such as `C.f()`) or on an instance (such as `C().f()`).
    > The instance is ignored except for its class.
    > If a class method is called for a derived class,
    > the derived class object is passed as the implied first argument.

`@staticmethod` and `@classmethod` are built-in to the interpreter
as they do not have implementations in Python code.
They are also the first decorators for the language, introduced in 2.2,
even before the decorator syntax was finalized.

When used, they have to be the outermost (top) decorator,
because they turn methods into special `staticmethod` and `classmethod` objects.

[Prev](../README.md) /
[Up](../README.md) /
[Next](../2-property/README.md)
