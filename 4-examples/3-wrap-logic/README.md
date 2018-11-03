# Examples

A decorator can be used to wrap a simple piece of logic to the decorated function.

It does so by creating a new function, injecting the logic,
and calling the original function to retrieve the result.

* Example 1

    >     def require_http_methods(request_method_list):
    >         """
    >         Decorator to make a view only accept particular request methods.  Usage::
    >
    >             @require_http_methods(["GET", "POST"])
    >             def my_view(request):
    >                 # I can assume now that only GET or POST requests make it this far
    >                 # ...
    >
    >         Note that request methods should be in uppercase.
    >         """
    >         def decorator(func):
    >             @wraps(func, assigned=available_attrs(func))
    >             def inner(request, *args, **kwargs):
    >                 if request.method not in request_method_list:
    >                     logger.warning(
    >                         'Method Not Allowed (%s): %s', request.method, request.path,
    >                         extra={'status_code': 405, 'request': request}
    >                     )
    >                     return HttpResponseNotAllowed(request_method_list)
    >                 return func(request, *args, **kwargs)
    >             return inner
    >         return decorator
    >
    >     require_GET = require_http_methods(["GET"])
    >     require_GET.__doc__ = "Decorator to require that a view only accepts the GET method."
    >
    >     require_POST = require_http_methods(["POST"])
    >     require_POST.__doc__ = "Decorator to require that a view only accepts the POST method."

        from django.views.decorators.http import require_GET, require_POST
        from django.contrib.auth.decorators import login_required
        from django.contrib.admin.views.decorators import staff_member_required
        from django.shortcuts import redirect, render
        from django.core.urlresolvers import reverse

        @require_GET
        def index(request):
            return HttpResponse("Hello, world!")

        @require_GET
        @login_required
        def dashboard(request):
            return render(request, 'dashboard.html')

        @require_POST
        @staff_member_required
        def add(request):
            # ...
            return redirect(reverse('dashboard'))

    For readability, it is often a good practice that this kind of decorator
    does not change the signature (i.e. parameters and return type) of the decorated function.
    In the example above each function is a Django view,
    and after being decorated they are still Django views.

* Example 2

    (Script available in <a href="https://github.com/MichaelKim0407/python-decorators/tree/master/4-examples/3-wrap-logic" target="_blank">repo</a>.)

        import time
        import functools

        def timed(func):
            @functools.wraps(func)
            def __new_func(*args, **kwargs):
                start = time.time()
                try:
                    return func(*args, **kwargs)
                finally:
                    end = time.time()
                    print(f"{func.__name__} took {end - start} seconds")

            return __new_func

        @timed
        def f(x):
            for i in range(10 ** x):
                pass

        if __name__ == '__main__':
            f(5)
            f(6)
            f(7)
            f(8)

[Prev](../2-register/README.md) /
[Up](../README.md) /
[Next](../4-generator/README.md)
