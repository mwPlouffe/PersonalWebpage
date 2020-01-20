from django.http import JsonResponse
from server.models import Association
from django.core import serializers


def index(req):
    data = Association.objects.all()
    data = serializers.serialize('json', data)
    print(data)
    return JsonResponse(data, safe=False)
