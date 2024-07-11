from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import TripsModel, ParticipantsModel, ActivitiesModels, LinksModel
from .serializers import (
    TripsSerializer, TripCreateSerializer, ParticipantsSerializer, 
    ActivitiesSerializer, LinksSerializer
)

class TripsViewSet(viewsets.ModelViewSet):
    queryset = TripsModel.objects.all()
    serializer_class = TripsSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return TripCreateSerializer
        return TripsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        trip = serializer.save()

        owner_name = serializer.validated_data.get('owner_name')
        owner_email = serializer.validated_data.get('owner_email')
        emails_to_invite = serializer.validated_data.get('emails_to_invite')

        ParticipantsModel.objects.create(
            trip_id=trip,
            name=owner_name,
            email=owner_email,
            is_confirmed=True,
            is_owner=True
        )

        for email in emails_to_invite:
            ParticipantsModel.objects.create(
                trip_id=trip,
                email=email,
                is_confirmed=False,
                is_owner=False
            )

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

class ParticipantsViewSet(viewsets.ModelViewSet):
    queryset = ParticipantsModel.objects.all()
    serializer_class = ParticipantsSerializer

    @action(detail=True, methods=['get'], url_path='trip')
    def trip_participants(self, request, pk=None):
        trip = self.get_object()
        participants = trip.participants.all()
        serializer = self.get_serializer(participants, many=True)
        return Response(serializer.data)

class ActivitiesViewSet(viewsets.ModelViewSet):
    queryset = ActivitiesModels.objects.all()
    serializer_class = ActivitiesSerializer

class LinksViewSet(viewsets.ModelViewSet):
    queryset = LinksModel.objects.all()
    serializer_class = LinksSerializer
