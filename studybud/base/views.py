from django.shortcuts import render
from .models import Room

""" rooms = [
    {'id':1, "name":"Discuss about python"},
    {'id':2, "name":"anything about UX"},
    {'id':3, "name":"lessons on node.js"},
] """



def home(request):
    #fetch all rooms from DB
    rooms = Room.objects.all()

    context = {"rooms" : rooms}
    return render(request, "base/home.html", context)

def room(request, pk):
    #fetch the room with the id as pk
    room = Room.objects.get(id = pk)                #get room info where id = pk

    context = {"room" : room}                       #send room to frontend
    return render(request, "base/room.html", context)