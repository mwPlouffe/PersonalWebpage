from django.http import JsonResponse
from server.models import Skill, SKILLS_QUALIFICATIONS


def operatingSystems(req):
    oses = Skill.objects.filter(type=SKILLS_QUALIFICATIONS[0][1])
    return JsonResponse(list(oses), safe=False)


def applications(req):
    apps = Skill.objects.filter(type=SKILLS_QUALIFICATIONS[1][1])
    return JsonResponse(list(apps), safe=False)


def programmingLanguages(req):
    langs = Skill.objects.filter(type=SKILLS_QUALIFICATIONS[2][1])
    return JsonResponse(list(langs), safe=False)


def platforms(req):
    plats = Skill.objects.filter(type=SKILLS_QUALIFICATIONS[3][1])
    return JsonResponse(list(plats), safe=False)


def methodologies(req):
    meths = Skill.objects.filter(type=SKILLS_QUALIFICATIONS[4][1])
    return JsonResponse(list(meths), safe=False)


def languages(req):
    langs = Skill.objects.filter(type=SKILLS_QUALIFICATIONS[5][1])
    return JsonResponse(list(langs), safe=False)


def licenses(req):
    lics = Skill.objects.filter(type=SKILLS_QUALIFICATIONS[6][1])
    return JsonResponse(list(lics), safe=False)
