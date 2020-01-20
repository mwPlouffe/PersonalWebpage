from django.http import JsonResponse
from server.models import Education, EducationNote
from django.core import serializers


def shortEducation(req):
    data = Education.objects.all()
    data = serializers.serialize('json', data)
    print(data)
    return JsonResponse(data, safe=False)


def longEducation(req):
    education = Education.objects.all()
    data = []
    for ed in education:
        notes = EducationNote.objects.filter(education=ed.id)
        data.append({
            'education': serializers.serialize('json', [ed]),
            'notes': serializers.serialize('json', notes)})
    print(data)
    return JsonResponse(data, safe=False)
