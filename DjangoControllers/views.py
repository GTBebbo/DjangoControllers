from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def get(request):
    return HttpResponse("This is a GET request", status=200)


@csrf_exempt
def post(request):
    return HttpResponse("This is a POST request", status=200)


@csrf_exempt
def put(request):
    return HttpResponse("This is a PUT request", status=200)


@csrf_exempt
def patch(request):
    return HttpResponse("This is a PATCH request", status=200)


@csrf_exempt
def delete(request):
    return HttpResponse("This is a DELETE request", status=200)


@csrf_exempt
def random(request):
    return HttpResponse("This is a RANDOM request", status=200)
