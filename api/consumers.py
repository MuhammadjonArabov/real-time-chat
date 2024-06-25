import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class ChatConsumers(AsyncJsonWebsocketConsumer):

    async def connect(self):   # Ulanishni taminlaydi
        self.room_name = self.scope['url_router']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code): # Xabar yuborish
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data): # Chatdan uzilish
        text_data_json = json.load(text_data)
        message = text_data_json['message']

        await self.channel_layer.group_send(self.room_group_name, {
            'type': 'chat_message',
            'message': message
        })

    async def chat_message(self, event): # Xabarno olish
        message = event['message']

        await self.send(text_data=json.dumps({'message': message}))
