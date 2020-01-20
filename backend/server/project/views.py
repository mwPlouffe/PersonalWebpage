from django.http import JsonResponse
from server.models import Project, ProjectNote
from django.core import serializers


def shortProject(req):
    data = Project.objects.filter(personal=True)
    data = serializers.serialize('json', data)
    print(data)
    return JsonResponse(data, safe=False)


def longProject(req):
    shorts = Project.objects.filter(personal=True)
    data = []
    for short in shorts:
        notes = ProjectNote.objects.filter(project=short.id)
        data.append({
            'project': serializers.serialize('json', [short]),
            'notes': serializers.serialize('json', notes)
        })
    print(data)
    return JsonResponse(data, safe=False)


def shortAcademicProject(req):
    data = Project.objects.filter(personal=False)
    data = serializers.serialize('json', data)
    print(data)
    return JsonResponse(data, safe=False)


def longAcademicProject(req):
    shorts = Project.objects.filter(personal=False)
    data = []
    for short in shorts:
        notes = ProjectNote.objects.filter(project=short.id)
        data.append({
            'project': serializers.serialize('json', [short]),
            'notes': serializers.serialize('json', notes)
        })
    print(data)
    return JsonResponse(data, safe=False)
