# Examples

Generator is a special type of function in Python that behaves as an iterator.
It is both easier to read and more efficient than using `list.append`
when building an iterable.

However in some cases a generator by itself may not fulfill what is needed.
In this case it can be combined with decorators to achieve more complex functionality.

(Executable scripts available in [repo](https://github.com/MichaelKim0407/python-decorators/tree/master/4-examples/4-generator).)
<!-- Stupid GitHub does not render `target="_blank"` written in Markdown, so you need to right click -->

* Example 1

        def execute(type=tuple):
            """
            Execute a generator and store results in a storage (default is tuple)
            """

            def __decor(gen):
                @functools.wraps(gen)
                def __new_func(*args, **kwargs):
                    return type(gen(*args, **kwargs))

                return __new_func

            return __decor

        @execute()
        def read_all(path):
            for line in read_lines(path):
                if line.startswith('#'):
                    continue
                yield line

* Example 2

        def partial(
                empty_error: Union[bool, Type[Exception]] = False
        ):
            """
            Decorates a generator so that when called,
            it's partially executed until the first `yield` statement.

            If the result is empty (i.e. a `yield` statement is never reached),
            0. The generator will be fully executed; and
            1. If `empty_error` is False (default), an empty tuple will be returned; otherwise
            2. If `empty_error` is True, a StopIteration will be raised; otherwise
            3. `empty_error()` will be raised
            """

            def __decor(gen):
                @functools.wraps(gen)
                def __new_func(*args, **kwargs):
                    iterator = gen(*args, **kwargs)
                    try:
                        first = next(iterator)
                    except StopIteration:
                        if not empty_error:
                            return ()
                        elif isinstance(empty_error, bool):
                            # empty_error = True
                            raise
                        else:
                            raise empty_error()

                    def __new_generator():
                        yield first
                        for item in iterator:
                            yield item

                    return __new_generator()

                return __new_func

            return __decor

        class Float(Exception):
            pass

        @partial()
        def read_int(path):
            for line in read_lines(path):
                if line.startswith('#'):
                    if 'float' in line:
                        raise Float
                    continue
                try:
                    yield int(line)
                except ValueError:
                    continue

        def read_float(path):
            for line in read_lines(path):
                if line.startswith('#'):
                    continue
                try:
                    yield float(line)
                except ValueError:
                    continue

        def read(path):
            try:
                return read_int(path)
            except Float:
                return read_float(path)

* Example 3

        def report(log=print, name=None, interval=1000):
            """
            Report progress of a generator
            """

            def __decor(gen):
                _name = name or gen.__name__

                @functools.wraps(gen)
                def __new_func(*args, **kwargs):
                    count = 0
                    for item in gen(*args, **kwargs):
                        yield item
                        count += 1
                        if count % interval == 0:
                            log("{}: yielded {} entries".format(_name, count))
                    log("{}: finished with {} entries".format(_name, count))

                return __new_func

            return __decor

        @report()
        def read(path):
            for line in read_lines(path):
                if line.startswith('#'):
                    continue
                yield line

[Prev](../3-wrap-logic/README.md) /
[Up](../README.md) /
[Next](../5-class/README.md)
