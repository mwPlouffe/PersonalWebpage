from django.http import JsonResponse
from server.models import Interest, INTERESTS


def ExperienceAbroad():
    exps = list(Interest.objects.filter(type=INTERESTS[0][1]))
    return JsonResponse(exps, safe=False)


def Literature():
    exps = list(Interest.objects.filter(type=INTERESTS[1][1]))
    return JsonResponse(exps, safe=False)


def Sports():
    exps = list(Interest.objects.filter(type=INTERESTS[2][1]))
    return JsonResponse(exps, safe=False)


def Passions():
    exps = list(Interest.objects.filter(type=INTERESTS[3][1]))
    return JsonResponse(exps, safe=False)
