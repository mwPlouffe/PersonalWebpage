from server.models import Skill
from server.serializers import SkillSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class SkillView(viewsets.ViewSet):
    def list(self, req):
        queryset = Skill.objects.all()
        serializer = SkillSerializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)
