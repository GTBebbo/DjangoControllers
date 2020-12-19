=================
DjangoControllers
=================

DjangoControllers is a Python package to extend Django's URL pattern functionality
with method dependent views like in Laravel.
It enables the ability to define specific view functions for each method in a path,
and will gracefully return 405 Method Not Allowed Response with a populated
"Allow" header based on the methods defined ion the path

Detailed documentation is in the "docs" directory.

Why Use DjangoControllers over Django's Class based Views?
----------------------------------------------------------

DjangoControllers offers more flexibility when defining views for each request method.
Class Based Views are constrained to handling a single endpoint. With DjangoControllers
you can create a Controller file to store all your views that control a model without
having to create multiple classes for DetailView and ListView.

DjangoControllers promotes more readable code, and better project structure.
It also removes the repetitive need to check the request method in every view.

See how DjangoControllers instantly tell you what methods a URL pattern supports and
what functions each method calls, from within your URLconf files::

    urlpatterns = [
        path(
            'my-endpoint/',
            include([
                path(
                    '',
                    Methods(
                        GET=ExampleController.get_view,
                        POST=ExampleController.post_view,
                        DELETE=ExampleController.delete_view,
                    )
                ),
                path(
                    '<int:model_id>/',
                    Methods(
                        GET=ExampleController.get_specific_view,
                    ),
                ),
            ]),
        ),
    ]

vs Class Based Views::

    urlpatterns = [
        path(
            'my-endpoint/',
            include([
                path(
                    '',
                    MyClassBasedView.as_view(),
                ),
                path(
                    '<int:model_id>/',
                    OtherClassBasedView.as_view(),
                ),
            ]),
        ),
    ]


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
