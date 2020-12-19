from os import environ

from django.http import HttpResponse

from DjangoControllers.exceptions import MethodNotAllowed


class Methods:

    def __init__(self, GET=None, POST=None, PUT=None, PATCH=None, DELETE=None, OPTIONS=None, HEAD=None, **kwargs):
        self.funcs = {
            'GET': GET,
            'POST': POST,
            'PUT': PUT,
            'PATCH': PATCH,
            'DELETE': DELETE,
            'OPTIONS': self.options if OPTIONS is None else OPTIONS,
            'HEAD': self.head if HEAD is None and GET is not None else HEAD,
            **kwargs,
        }
        self.method = None

    @property
    def allowed_methods(self):
        """
        Return a list of allowed methods for the endpoint
        """
        return [method for method, func in self.funcs.items() if func is not None]

    def set_method(self, method):
        """
        Set method string of request for use on functions such as __getattr__
        """
        self.method = method
        try:
            if self.funcs[self.method] is None:
                # If function for method has not been defined, raise a 405 Method Not Allowed Exception
                raise MethodNotAllowed(allowed_methods=self.allowed_methods)
        except (TypeError, IndexError):
            # If function for method has not been defined, raise a 405 Method Not Allowed Exception
            raise MethodNotAllowed(allowed_methods=self.allowed_methods)

    def options(self, request, *args, **kwargs):
        """Handle responding to requests for the OPTIONS HTTP verb."""
        response = HttpResponse()
        response['Accept'] = ', '.join(self.allowed_methods)
        response['Content-Length'] = 0
        return response

    def head(self, request, *args, **kwargs):
        """Handle responding to requests for the HEAD HTTP verb."""
        response = self.funcs['GET'](request, *args, **kwargs)
        response['Content-Length'] = 0
        response.body = ""
        return response

    def __getattr__(self, item):
        # Use method to forward on possible attributes
        # set by decorators like csrf_exempt
        return getattr(self.funcs[self.method] if self.method else None, item)

    def __call__(self, request, *args, **kwargs):
        try:
            response = self.funcs[request.method](request, *args, **kwargs)
        except (TypeError, IndexError):
            # If function for method has not been defined, raise a 405 Method Not Allowed Exception
            raise MethodNotAllowed(allowed_methods=self.allowed_methods)
        return response
