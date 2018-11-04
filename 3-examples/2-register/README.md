# Examples

## Registering an item

Decorators can be used to register an item without changing it.

> ```python
> def route(self, rule, **options):
>     """A decorator that is used to register a view function for a
>     given URL rule.  This does the same thing as :meth:`add_url_rule`
>     but is intended for decorator usage::
>
>         @app.route('/')
>         def index():
>             return 'Hello World'
>
>     For more information refer to :ref:`url-route-registrations`.
>
>     :param rule: the URL rule as string
>     :param endpoint: the endpoint for the registered URL rule.  Flask
>                      itself assumes the name of the view function as
>                      endpoint
>     :param options: the options to be forwarded to the underlying
>                     :class:`~werkzeug.routing.Rule` object.  A change
>                     to Werkzeug is handling of method options.  methods
>                     is a list of methods this rule should be limited
>                     to (``GET``, ``POST`` etc.).  By default a rule
>                     just listens for ``GET`` (and implicitly ``HEAD``).
>                     Starting with Flask 0.6, ``OPTIONS`` is implicitly
>                     added and handled by the standard request handling.
>     """
>     def decorator(f):
>         endpoint = options.pop('endpoint', None)
>         self.add_url_rule(rule, endpoint, f, **options)
>         return f
>     return decorator
> ```

```python
from flask import Flask

app = Flask('app')

@app.route('/')
def index():
    return "Hello, world!"
```

As can be seen in the definition of `route`,
using this decorator does not change the function itself,
so we may (if we want to) still use it as a regular function:

```python
def test():
    print(index())
```

When using decorators in this way,
it is important to import all modules that include a registry,
if your code is broken down into multiple files.

(Executable script available in [repo](https://github.com/MichaelKim0407/python-decorators/tree/master/3-examples/2-register).)

```python
# app.py
from flask import Flask

app = Flask('app')
```

```python
# api.py
from app import app

@app.route('/api/')
def api_root():
    return "This api contains ..."
```

```python
# main.py
from app import app
import api  # try removing this line and then visit /api

@app.route('/')
def index():
    return '<a href="/api">api</a>'

if __name__ == '__main__':
    app.run()
```

[Prev](../1-annotate/README.md) /
[Up](../README.md) /
[Next](../3-wrap-logic/README.md)
