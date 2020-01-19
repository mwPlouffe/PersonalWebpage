from django.http import JsonResponse
from server.models import Association


def index(req):
    assocs = list(Association.objects.all())
    return JsonResponse(assocs, safe=False)
