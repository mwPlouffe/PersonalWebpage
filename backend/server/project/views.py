from django.http import JsonResponse
from server.models import Project, ProjectNote


def shortProject(req):
    projects = list(Project.objects.filter(personal=False))
    return JsonResponse(projects, safe=False)


def longProject(req):
    shorts = list(Project.objects.filter(personal=False))
    projects = []
    for short in shorts:
        notes = ProjectNote.objects.filter(project=short.id)
        projects.append((short, notes))
    return JsonResponse(projects, safe=False)


def shortAcademicProject(req):
    projects = list(Project.objects.filter(personal=True))
    return JsonResponse(projects, safe=False)


def longAcademicProject(req):
    shorts = list(Project.objects.filter(personal=True))
    projects = []
    for short in shorts:
        notes = ProjectNote.objects.filter(project=short.id)
        projects.append((short, notes))
    return JsonResponse(projects, safe=False)
