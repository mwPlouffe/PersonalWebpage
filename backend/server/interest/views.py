from server.models import Interest
from server.serializers import InterestSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class InterestView(viewsets.ViewSet):
    def list(self, req):
        queryset = Interest.objects.all()
        serializer = InterestSerializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)
