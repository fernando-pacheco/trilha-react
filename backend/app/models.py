from django.db import models

class TripsModel(models.Model):
    destination = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    owner_name = models.CharField(max_length=255)
    owner_email = models.EmailField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.destination} from {self.start_date} to {self.end_date}"

class EmailsToInviteModel(models.Model):
    trip = models.ForeignKey(TripsModel, related_name='invites', on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.email

class LinksModel(models.Model):
    trip = models.ForeignKey(TripsModel, related_name='links', on_delete=models.CASCADE)
    link = models.URLField()

    def __str__(self):
        return self.link
