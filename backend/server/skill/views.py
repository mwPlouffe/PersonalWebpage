from django.http import JsonResponse
from server.models import Skill, SKILLS_QUALIFICATIONS
from django.core import serializers


def operatingSystems(req):
    data = Skill.objects.filter(type=SKILLS_QUALIFICATIONS[0][0])
    data = serializers.serialize('json', data)
    print(data)
    return JsonResponse(data, safe=False)


def applications(req):
    data = Skill.objects.filter(type=SKILLS_QUALIFICATIONS[1][0])
    data = serializers.serialize('json', data)
    print(data)
    return JsonResponse(data, safe=False)


def programmingLanguages(req):
    data = Skill.objects.filter(type=SKILLS_QUALIFICATIONS[2][0])
    data = serializers.serialize('json', data)
    print(data)
    return JsonResponse(data, safe=False)


def platforms(req):
    data = Skill.objects.filter(type=SKILLS_QUALIFICATIONS[3][0])
    data = serializers.serialize('json', data)
    print(data)
    return JsonResponse(data, safe=False)


def methodologies(req):
    data = Skill.objects.filter(type=SKILLS_QUALIFICATIONS[4][0])
    data = serializers.serialize('json', data)
    print(data)
    return JsonResponse(data, safe=False)


def languages(req):
    data = Skill.objects.filter(type=SKILLS_QUALIFICATIONS[5][0])
    data = serializers.serialize('json', data)
    print(data)
    return JsonResponse(data, safe=False)


def licenses(req):
    data = Skill.objects.filter(type=SKILLS_QUALIFICATIONS[6][0])
    data = serializers.serialize('json', data)
    print(data)
    return JsonResponse(data, safe=False)
