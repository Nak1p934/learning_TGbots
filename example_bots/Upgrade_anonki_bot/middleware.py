from time import time
from aiogram import BaseMiddleware

class AntiSpamMiddleware(BaseMiddleware):
    def __init__(self):
        self.last_time = {}

    async def __call__(self, handler, event, data):
        user_id = event.from_user.id
        now = time()

        if user_id in self.last_times and now - self.last_times[user_id] < 1:
            return

        self.last_time[user_id] = now
        return await handler(event, data)