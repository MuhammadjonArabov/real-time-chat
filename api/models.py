from django.db import models
from django.utils import timezone


class Message(models.Model):
    room = models.CharField(max_length=300)
    author = models.CharField(max_length=300)
    connect = models.TextField()
    time_stamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.author}: {self.connect}'
