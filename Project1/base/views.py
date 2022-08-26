from django.shortcuts import render
# from django.http import HttpResponse
from .models import Room
# Create your views here.

queryset = Room.objects.filter(title="Project")


rooms = [

    {'id': 1, 'name': "Room1"},
    {'id': 2, 'name': "Room2"},
    {'id': 3, 'name': "Room3"},
    {'id': 4, 'name': "Room4"},
]


def home(req):
    # return HttpResponse("Home")
    context = {'rooms': rooms}
    return render(req, "base/home.html", context)


def room(req, no):
    # return HttpResponse("Room")
    for room in rooms:
        if room['id'] == no:
            context = {"room": room}
            break
    return render(req, "base/room.html", context)
