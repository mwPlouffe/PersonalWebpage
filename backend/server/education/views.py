from django.http import JsonResponse
from server.models import Education, EducationNote


def shortEducation(req):
    education = Education.objects.all()
    return JsonResponse(list(education), safe=False)


def longEducation(req):
    education = list(Education.objects.all())
    data = []
    for ed in education:
        notes = EducationNote.objects.filter(education=ed.id)
        data.append((ed, notes))
    return JsonResponse(data, safe=False)
