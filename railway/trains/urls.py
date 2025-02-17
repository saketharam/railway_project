from django.urls import path
from .views import AddTrainView, GetTrainsView

urlpatterns = [
    path("add/", AddTrainView.as_view(), name="add_train"),
    path("search/", GetTrainsView.as_view(), name="get_trains"),
]
