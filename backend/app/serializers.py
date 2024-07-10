from rest_framework import serializers
from .models import TripsModel, EmailsToInviteModel, LinksModel

class EmailsToInviteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailsToInviteModel
        fields = '__all__'

class LinksModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinksModel
        fields = '__all__'

class TripsModelSerializer(serializers.ModelSerializer):
    invites = EmailsToInviteModelSerializer(many=True, read_only=True)
    links = LinksModelSerializer(many=True, read_only=True)

    class Meta:
        model = TripsModel
        fields = '__all__'
