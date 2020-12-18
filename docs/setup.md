# Setup

To setup DjangoControllers in your django project, first add the middleware to your `settings.py`:

```python
middleware = [
    'django.middleware.security.SecurityMiddleware',
    'DjangoControllers.middleware.MethodMiddleware',
    ...
    'django.middleware.csrf.CsrfViewMiddleware',
    ...
]
```

NB: The middleware must be above all middleware that utilises the `process_view()` hook. By default the first middleware
that uses this hook is the csrf middleware. To be safe we recommend you place the DjangoControllers middleware directly
below the django Security middleware.

Next, import the `Methods` class into all `urls.py` files in which you wish to use define
paths with method dependent views.

```python
from DjangoControllers.urls import Methods
```

Finally, to create your first method dependent view, use a `Methods` object as your view in the `url_patterns`:

```python
url_patterns = [
    path('my-endpoint/', Methods(
        GET=MyController.my_view
    ))
]
```
