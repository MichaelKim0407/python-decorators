# Why decorators?

## The way we read

It is important to realize that,
while modularity and DRY can be achieved through other means,
the decorator syntax itself has opened the possibility of
creating simple, clean and elegant solutions.

It has a lot to do with the way we are trained to read code -
from top to bottom.

Compare the following two pieced of code:

```python
def dashboard(request):
    return render(request, 'dashboard.html')

dashboard = require_GET(login_required(dashboard))
```

```python
@require_GET
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
```

They might not seem very different here,
but often the decorated function will be much longer.

In the first snippet, the extra information -
the view requires user login, and requires GET method -
are not provided when reading the function body,
and if you know that it should require these restrictions,
you will have that doubt until after you finish reading,
or you'll have to counter-intuitively read the last line first.

In the second snippet however,
the extra information are provided at the beginning of the function definition,
so when reading the body you'll know that they have already been taken care of.

[Prev](../2-modular/README.md) /
[Up](../README.md) /
[Next](../4-when-not/README.md)
