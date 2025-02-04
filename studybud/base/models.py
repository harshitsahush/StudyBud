from django.db import models
from django.contrib.auth.models import User             #using django's default user model


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null = True)        #assuming a room has only one topic
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)           #null allows empty in DB, blank allows empty in forms
    #participants = 
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Message(models.Model):
    user = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:50]           #we want to show only first 50 chars