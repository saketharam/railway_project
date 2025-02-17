from django.db import models

class Train(models.Model):
    name = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    total_seats = models.IntegerField()
    available_seats = models.IntegerField()

    def __str__(self):
        return Train.name