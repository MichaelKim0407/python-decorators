# Why decorators?

## Modularity

Modularity goes hand-in-hand with the DRY principle.
When creating a complex logic, it is good practice to break it down,
and each piece of code should only do one thing.
By creating modular code we are also creating reusable code.

Compare the following two pieces of code:

```python
def dashboard(request):
    if request.method != 'GET':
        return HttpResponseMethodNotAllowed('GET')

    if request.user.is_anonymous:
        return redirect(request, reverse('login'))

    return render(request, 'dashboard.html')
```

```python
@require_GET
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
```

Or even this:

```python
def dashboard(request):
    if request.method == 'GET':
        if not request.user.is_anonymous:
            return render(request, 'dashboard.html')
        else:
            return redirect(request, reverse('login'))
    else:
        return HttpResponseMethodNotAllowed('GET')
```

The snippet with decorators has a very clear, untwisted logic.

[Prev](../1-dry/README.md) /
[Up](../README.md) /
[Next](../3-read/README.md)
