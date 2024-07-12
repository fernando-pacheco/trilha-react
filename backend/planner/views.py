from rest_framework import viewsets, status
from collections import defaultdict
from rest_framework.response import Response
from dateutil.parser import parse as parse_datetime
from .models import TripsModel, ParticipantsModel, ActivitiesModels, LinksModel
from django.utils.timezone import make_aware, is_naive
from django.utils import timezone
from datetime import datetime
from uuid import UUID
from django.shortcuts import get_object_or_404
import pytz
from .serializers import (
    TripsSerializer, TripCreateSerializer, ParticipantsSerializer, 
    ActivitiesSerializer, LinksSerializer
)


class TripsViewSet(viewsets.ModelViewSet):
    queryset = TripsModel.objects.all()
    serializer_class = TripsSerializer

    def retrieve(self, request, *args, **kwargs):
        tripId = str(kwargs.get('tripId')).replace('-', '')
        trip = get_object_or_404(TripsModel, id=tripId)

        if not trip:
            return Response({'message': 'Trip not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(trip)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'create':
            return TripCreateSerializer
        return TripsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        sao_paulo_tz = pytz.timezone('America/Sao_Paulo')
        current_datetime = timezone.now().astimezone(sao_paulo_tz)

        starts_at = data['starts_at']
        ends_at = data['ends_at']

        if isinstance(starts_at, str):
            starts_at = parse_datetime(starts_at)
        if isinstance(ends_at, str):
            ends_at = parse_datetime(ends_at)

        if is_naive(starts_at):
            starts_at = make_aware(starts_at, sao_paulo_tz)
        if is_naive(ends_at):
            ends_at = make_aware(ends_at, sao_paulo_tz)

        if starts_at < current_datetime:
            return Response({'message': 'Invalid trip start date.'}, status=status.HTTP_400_BAD_REQUEST)

        if ends_at < starts_at:
            return Response({'message': 'Invalid trip end date.'}, status=status.HTTP_400_BAD_REQUEST)
        
        trip = TripsModel.objects.create(
            destination=data['destination'],
            starts_at=starts_at,
            ends_at=ends_at,
        )

        ParticipantsModel.objects.create(
            trip=trip,
            name=data['owner_name'],
            email=data['owner_email'],
            is_confirmed=True,
            is_owner=True
        )

        for email in data.get('emails_to_invite', []):
            ParticipantsModel.objects.create(
                trip=trip,
                email=email,
                is_confirmed=False,
                is_owner=False
            )

        serializer_data = TripsSerializer(trip).data
        headers = self.get_success_headers(serializer.data)
        
        return Response(serializer_data, status=status.HTTP_201_CREATED, headers=headers)

class ParticipantsViewSet(viewsets.ModelViewSet):
    queryset = ParticipantsModel.objects.all()
    serializer_class = ParticipantsSerializer

    def all(self, request, *args, **kwargs):
        return Response(self.serializer_class(self.queryset, many=True).data)

    def retrieve(self, request, *args, **kwargs):
        participantId = str(kwargs.get('participantId')).replace('-', '')
        participant = get_object_or_404(ParticipantsModel, id=participantId)

        if not participant:
            return Response({'message': 'Participant not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(participant)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        tripId = str(kwargs.get('tripId')).replace('-', '')
        queryset = self.queryset.filter(trip_id=tripId)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

class ActivitiesViewSet(viewsets.ModelViewSet):
    queryset = ActivitiesModels.objects.all()
    serializer_class = ActivitiesSerializer

    def all(self, request, *args, **kwargs):
        return Response(self.serializer_class(self.queryset, many=True).data)

    def list(self, request, *args, **kwargs):
        tripId = str(kwargs.get('tripId')).replace('-', '')
        queryset = self.queryset.filter(trip_id=tripId)
        grouped_activities = defaultdict(list)

        for activity in queryset:
            grouped_activities[activity.occurs_at.date()].append(activity)

        sorted_dates = sorted(grouped_activities.keys())

        response_data = []
        for date in sorted_dates:
            activities_for_date = grouped_activities[date]
            serialized_activities = ActivitiesSerializer(activities_for_date, many=True).data
            response_data.append({
                'date': date,
                'activities': serialized_activities
            })

        return Response(response_data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data

        trip = TripsModel.objects.get(id=data['trip'])
        occurs_at = datetime.strptime(data['occurs_at'], '%d/%m/%Y %H:%M')

        sao_paulo_tz = pytz.timezone('UTC')
        occurs_at = make_aware(occurs_at, sao_paulo_tz)

        if not trip:
            return Response({'message': 'Trip not found.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        if not trip.starts_at < occurs_at < trip.ends_at:
            return Response({'message': 'Invalid activity date.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        activity = ActivitiesModels.objects.create(
            title=data['title'],
            occurs_at=occurs_at,
            trip=trip
        )

        serializer_data = ActivitiesSerializer(activity).data
        headers = self.get_success_headers(serializer.data)
        
        return Response(serializer_data, status=201, headers=headers)

class LinksViewSet(viewsets.ModelViewSet):
    queryset = LinksModel.objects.all()
    serializer_class = LinksSerializer

    def list(self, request, *args, **kwargs):
        tripId = str(kwargs.get('tripId')).replace('-', '')
        queryset = self.queryset.filter(trip_id=tripId)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
    def all(self, request, *args, **kwargs):
        return Response(self.serializer_class(self.queryset, many=True).data)
        
