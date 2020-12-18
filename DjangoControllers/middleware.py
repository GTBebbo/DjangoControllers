from django.http import HttpResponse

from DjangoControllers.exceptions import MethodNotAllowed
from DjangoControllers.urls import Methods


class MethodMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
        except MethodNotAllowed as e:
            # If not in debug mode, return a Method Not Allowed response with appropriate allow header
            response = HttpResponse(status=405)
            response['Allow'] = ", ".join(e.allowed_methods)
        return response

    @staticmethod
    def process_view(request, callback, callback_args, callback_kwargs):
        """
        Set the method of the callback such that the attributes can be forwarded on
        if the callback is of type ControllerMethods
        """
        if isinstance(callback, Methods):
            try:
                callback.set_method(request.method)
            except MethodNotAllowed as e:
                # If not in debug mode, return a Method Not Allowed response with appropriate allow header
                response = HttpResponse(status=405)
                response['Allow'] = ", ".join(e.allowed_methods)
                return response
