from django.http import JsonResponse
from server.models import Interest, INTERESTS
from django.core import serializers


def ExperienceAbroad(req):
    data = Interest.objects.filter(type=INTERESTS[0][0])
    data = serializers.serialize('json', data)
    print(data)
    return JsonResponse(data, safe=False)


def Literature(req):
    data = Interest.objects.filter(type=INTERESTS[1][0])
    data = serializers.serialize('json', data)
    print(data)
    return JsonResponse(data, safe=False)


def Sports(req):
    data = Interest.objects.filter(type=INTERESTS[2][0])
    data = serializers.serialize('json', data)
    print(data)
    return JsonResponse(data, safe=False)


def Passions(req):
    data = Interest.objects.filter(type=INTERESTS[3][0])
    data = serializers.serialize('json', data)
    print(data)
    return JsonResponse(data, safe=False)
