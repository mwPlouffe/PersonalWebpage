from rest_framework import viewsets
from rest_framework.response import Response


class DefaultView(viewsets.GenericViewSet):
    def index(self, req):
        return Response('Index Page!')
