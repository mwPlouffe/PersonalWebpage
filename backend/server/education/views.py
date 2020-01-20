from server.serializers import EducationSerializer
from server.models import Education, EducationNote
from rest_framework import viewsets
from rest_framework.response import Response


class EducationView(viewsets.ModelViewSet):
    def shortList(self, req):
        data = Education.objects.all()
        serializer = EducationSerializer(data, many=True)
        return Response(serializer.data)


    def longList(self, req):
        education = Education.objects.all()
        serializer = EducationSerializer(data, many=True)
