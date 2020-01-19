from django.http import HttpResponse


def index(req):
    return HttpResponse('Index Page!')

