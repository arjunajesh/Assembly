from django.urls import path, include
from . import views

urlpatterns = [
    path("getevents/", views.get_reccomended_events)
]