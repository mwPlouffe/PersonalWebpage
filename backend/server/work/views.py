from server.models import Work, WorkNote
from server.serializers import WorkSerializer, WorkNoteSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class WorkView(viewsets.ViewSet):
    def list(self, req):
        print(req.GET)

        paid = req.GET.get('paid') is not None
        volunteer = req.GET.get('volunteer') is not None
        short = req.GET.get('short') is not None

        if paid and not volunteer:
            works = Work.objects.filter(volunteer=False)
        elif volunteer and not paid:
            works = Work.objects.filter(volunteer=True)
        else:
            works = Work.objects.all()

        if short:
            serializer = WorkSerializer(works, many=True)
            print(serializer.data)
            return Response(serializer.data)

        data = []
        for w in works:
            notes = WorkNote.objects.filter(work=w.id)
            data.append({
                'work': WorkSerializer(w, many=False).data,
                'notes': WorkNoteSerializer(notes, many=True).data
            })
        print(data)
        return Response(data)
