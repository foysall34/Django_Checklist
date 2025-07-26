# chat/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({
            'message': 'Connected to WebSocket!'
        }))

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get("message")

        # Echo back
        await self.send(text_data=json.dumps({
            'message': message
        }))



