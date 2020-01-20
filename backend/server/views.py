from django.http import HttpResponse
from django.core import serializers


def index(req):
    return HttpResponse('Index Page!')
