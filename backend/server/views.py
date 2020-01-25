from rest_framework import viewsets
from rest_framework.response import Response


class DefaultView(viewsets.GenericViewSet):
    def list(self, req):
        return Response('Index Page!')
