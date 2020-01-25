from server.models import Education, EducationNote
from server.serializers import EducationSerializer, EducationNoteSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class EducationView(viewsets.ViewSet):
    def list(self, req):
        print(req.GET)
        short = req.GET.get('short') is not None

        educations = Education.objects.all()

        if short is True:
            serializer = EducationSerializer(educations, many=True)
            print(serializer.data)
            return Response(serializer.data)

        data = []
        for e in educations:
            notes = EducationNote.objects.filter(education=e.id)
            data.append({
                'education': EducationSerializer(e, many=False).data,
                'notes': EducationNoteSerializer(notes, many=True).data
            })
        print(data)
        return Response(data)
