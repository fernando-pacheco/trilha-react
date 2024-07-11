from rest_framework import serializers
from .models import TripsModel, ParticipantsModel, ActivitiesModels, LinksModel

class ParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantsModel
        fields = ['id', 'name', 'email', 'is_confirmed', 'is_owner', 'trip_id']

class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivitiesModels
        fields = ['id', 'title', 'occurs_at', 'trip_id']

class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinksModel
        fields = ['id', 'title', 'url', 'trip_id']

class TripsSerializer(serializers.ModelSerializer):
    participants = ParticipantsSerializer(many=True, read_only=True)
    activities = ActivitiesSerializer(many=True, read_only=True)
    urls = LinksSerializer(many=True, read_only=True)

    class Meta:
        model = TripsModel
        fields = ['id', 'destination', 'starts_at', 'ends_at', 'created_at', 'is_confirmed', 'participants', 'activities', 'urls']

class TripCreateSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField()
    owner_email = serializers.EmailField()
    emails_to_invite = serializers.ListField(child=serializers.EmailField())

    class Meta:
        model = TripsModel
        fields = ['destination', 'starts_at', 'ends_at', 'owner_name', 'owner_email', 'emails_to_invite']
