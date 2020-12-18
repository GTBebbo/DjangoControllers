=================
DjangoControllers
=================

DjangoControllers is a Django app to extend django's url pattern functionality
with method dependent views. It enables the ability to define specific view functions
for each method in a path, and will gracefully return 405 Method Not Allowed Response
with a populated "Allow" header based on the methods defined ion the path

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add the DjangoController middleware to your ``settings.py``
below the security middleware::

    middleware = [
        'django.middleware.security.SecurityMiddleware',
        'DjangoControllers.middleware.MethodMiddleware',
        ...
        'django.middleware.csrf.CsrfViewMiddleware',
        ...
    ]

**NB:** The DjangoController middleware must be **above** the CSRF middleware

2. Import the ``Methods`` class into your URLconf::

    DjangoControllers.urls import Methods

3. Define a path using the ``Methods`` class to specify view functions
for each method you wish to handle::

    path('my-endpoint/', Methods(
        GET=MyEndpointController.my_get_function,
        POST=MyEndpointController.my_post_function,
        DELETE=MyEndpointController.my_delete_function,
    )),
