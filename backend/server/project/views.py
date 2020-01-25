from server.models import Project, ProjectNote
from server.serializers import ProjectSerializer, ProjectNoteSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class ProjectView(viewsets.ViewSet):
    def list(self, req):
        print(req.GET)
        personal = req.GET.get('personal') is not None
        academic = req.GET.get('academic') is not None
        short = req.GET.get('short') is not None

        if personal and not academic:
            projects = Project.objects.filter(personal=True)
        elif academic and not personal:
            projects = Project.objects.filter(personal=False)
        else:
            projects = Project.objects.all()

        if short:
            serializer = ProjectSerializer(projects, many=True)
            print(serializer.data)
            return Response(serializer.data)

        data = []
        for p in projects:
            notes = ProjectNote.objects.filter(project=p.id)
            data.append({
                'project': ProjectSerializer(p, many=False).data,
                'notes': ProjectNoteSerializer(notes, many=True).data
            })
        print(data)
        return Response(data)
