from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def get_view(request):
    return HttpResponse("GET Request", status=200)


def get_specific_view(request, model_id):
    print("GET CALLED")
    return HttpResponse(f"GET Request for model id: {model_id}", status=200)


@csrf_exempt
def post_view(request):
    return HttpResponse("POST Request", status=200)


@csrf_exempt
def delete_view(request):
    return HttpResponse("DELETE Request", status=200)
