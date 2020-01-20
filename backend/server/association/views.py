from server.models import Association
from server.serializers import AssociationSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class AssociationView(viewsets.ViewSet):
    def list(self, req):
        queryset = Association.objects.all()
        serializer = AssociationSerializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)
