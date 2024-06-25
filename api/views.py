from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializers


class MessageAPIView(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializers
