from django.http import JsonResponse
from server.models import Work, WorkNote


def shortWork(req):
    work = list(Work.objects.filter(volunteer=False))
    return JsonResponse(work, safe=False)


def longWork(req):
    shorts = list(Work.objects.filter(volunteer=False))
    work = []
    for short in shorts:
        notes = WorkNote.objects.filter(project=short.id)
        work.append((short, notes))
    return JsonResponse(work, safe=False)


def shortVolunteerWork(req):
    work = list(Work.objects.filter(volunteer=True))
    return JsonResponse(work, safe=False)


def longVolunteerWork(req):
    shorts = list(Work.objects.filter(volunteer=True))
    work = []
    for short in shorts:
        notes = WorkNote.objects.filter(project=short.id)
        work.append((short, notes))
    return JsonResponse(work, safe=False)
