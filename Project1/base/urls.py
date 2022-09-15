from . import views
from django.urls import path

urlpatterns = [

    path("room/<int:no>/", views.room, name="Room"),
    path("", views.home, name="Home"),
]
