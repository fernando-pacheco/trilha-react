from rest_framework import viewsets
from .models import TripsModel, EmailsToInviteModel, LinksModel
from .serializers import TripsModelSerializer, EmailsToInviteModelSerializer, LinksModelSerializer

class TripsModelViewSet(viewsets.ModelViewSet):
    queryset = TripsModel.objects.all()
    serializer_class = TripsModelSerializer

class EmailsToInviteModelViewSet(viewsets.ModelViewSet):
    queryset = EmailsToInviteModel.objects.all()
    serializer_class = EmailsToInviteModelSerializer

class LinksModelViewSet(viewsets.ModelViewSet):
    queryset = LinksModel.objects.all()
    serializer_class = LinksModelSerializer
