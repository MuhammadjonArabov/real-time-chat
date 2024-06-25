from rest_framework import serializers
from .models import Message


class MessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'room', 'author', 'connect', 'time_stamp']
