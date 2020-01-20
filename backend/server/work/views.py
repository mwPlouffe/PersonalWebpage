from django.http import JsonResponse
from server.models import Work, WorkNote
from django.core import serializers


def shortWork(req):
    data = Work.objects.filter(volunteer=False)
    data = serializers.serialize('json', data)
    print(data)
    return JsonResponse(data, safe=False)


def longWork(req):
    work = Work.objects.filter(volunteer=False)
    data = []
    for w in work:
        notes = WorkNote.objects.filter(work=w.id)
        data.append({
            'work': serializers.serialize('json', [w]),
            'notes': serializers.serialize('json', notes)
        })
    print(data)
    return JsonResponse(data, safe=False)


def shortVolunteerWork(req):
    data = Work.objects.filter(volunteer=True)
    data = serializers.serialize('json', data)
    print(data)
    return JsonResponse(data, safe=False)


def longVolunteerWork(req):
    work = Work.objects.filter(volunteer=True)
    data = []
    for w in work:
        notes = WorkNote.objects.filter(work=w.id)
        data.append({
            'work': serializers.serialize('json', [w]),
            'notes': serializers.serialize('json', notes)
        })
    print(data)
    return JsonResponse(data, safe=False)
