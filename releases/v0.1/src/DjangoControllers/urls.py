from os import environ

from DjangoControllers.exceptions import MethodNotAllowed


class Methods:

    def __init__(self, GET=None, POST=None, PUT=None, PATCH=None, DELETE=None, **kwargs):
        self.funcs = {
            'GET': GET,
            'POST': POST,
            'PUT': PUT,
            'PATCH': PATCH,
            'DELETE': DELETE,
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
                raise MethodNotAllowed()
        except (TypeError, IndexError):
            # If function for method has not been defined, raise a 405 Method Not Allowed Exception
            raise MethodNotAllowed(allowed_methods=self.allowed_methods)

    def __getattr__(self, item):
        # Use method to forward on attributes
        return getattr(self.funcs[self.method] if self.method else None, item)

    def __call__(self, request, *args, **kwargs):
        try:
            response = self.funcs[request.method](request, *args, **kwargs)
        except (TypeError, IndexError):
            # If function for method has not been defined, raise a 405 Method Not Allowed Exception
            raise MethodNotAllowed(allowed_methods=self.allowed_methods)
        return response
