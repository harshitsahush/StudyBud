from django.shortcuts import render


def home(request):
    rooms = [
        {'id':1, "name":"Discuss about python"},
        {'id':2, "name":"anything about UX"},
        {'id':3, "name":"lessons on node.js"},
    ]

    context = {"rooms" : rooms}

    return render(request, "base/home.html", context)

def room(request):
    return render(request, "base/room.html")