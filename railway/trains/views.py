from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.conf import settings
from .models import Train
from .serializers import TrainSerializer

class AddTrainView(generics.CreateAPIView):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer

    def post(self, request, *args, **kwargs):
        api_key = request.headers.get("X-API-KEY")
        if api_key != settings.ADMIN_API_KEY:
            return Response({"error": "Unauthorized"}, status=403)
        return super().post(request, *args, **kwargs)

class GetTrainsView(generics.ListAPIView):
    serializer_class = TrainSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        source = self.request.query_params.get("source")
        destination = self.request.query_params.get("destination")
        return Train.objects.filter(source=source, destination=destination)
