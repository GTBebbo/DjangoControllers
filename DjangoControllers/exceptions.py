class MethodNotAllowed(Exception):

    def __init__(self, allowed_methods: list, msg: str = "405 Method Not Allowed"):
        Exception.__init__(self, msg)
        if not isinstance(allowed_methods, (list, tuple)):
            allowed_methods = []
        self.allowed_methods = allowed_methods
