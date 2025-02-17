from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import transaction
from .models import Booking
from trains.models import Train
from .serializers import BookingSerializer

class BookSeatView(APIView):
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def post(self, request):
        train_id = request.data.get("train_id")
        user = request.user

        try:
            train = Train.objects.select_for_update().get(id=train_id)
            if train.available_seats > 0:
                seat_number = train.total_seats - train.available_seats + 1
                train.available_seats -= 1
                train.save()

                booking = Booking.objects.create(user=user, train=train, seat_number=seat_number)
                return Response({"message": "Seat booked", "booking_id": booking.id})
            else:
                return Response({"error": "No seats available"}, status=400)
        except Train.DoesNotExist:
            return Response({"error": "Train not found"}, status=404)
