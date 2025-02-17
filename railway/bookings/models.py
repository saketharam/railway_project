from django.db import models
from django.contrib.auth import get_user_model
from trains.models import Train

User = get_user_model()

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
