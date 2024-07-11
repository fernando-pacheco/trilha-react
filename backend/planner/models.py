import uuid
from django.db import models


class TripsModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    destination = models.CharField(max_length=255)
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)


class ParticipantsModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    is_confirmed = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    trip_id = models.ForeignKey(TripsModel, related_name='participants', on_delete=models.CASCADE)


class ActivitiesModels(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    occurs_at = models.DateTimeField()
    trip_id = models.ForeignKey(TripsModel, related_name="activities", on_delete=models.CASCADE)


class LinksModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    url = models.URLField()
    trip_id = models.ForeignKey(TripsModel, related_name="urls", on_delete=models.CASCADE)
