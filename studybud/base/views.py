from django.shortcuts import render

rooms = [
    {'id':1, "name":"Discuss about python"},
    {'id':2, "name":"anything about UX"},
    {'id':3, "name":"lessons on node.js"},
]

def home(request):
    context = {"rooms" : rooms}
    return render(request, "base/home.html", context)

def room(request, pk):
    room = None
    for i in rooms:
        if(str(i['id']) == pk):
            room = i

    context = {"room" : room}                       #send room to frontend
    return render(request, "base/room.html", context)