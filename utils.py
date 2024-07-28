from typing import List
from aiogram.types import Message
from aiogram import exceptions
import asyncio


async def send_message_to_users(all_users_id: List[int], sending_message: Message, sleep: float = 0.05) -> int:
    async def send_message(user_id: int, message: Message) -> bool:
        success = False
        flood = False
        try:
            await message.send_copy(chat_id=user_id)
            success = True
        except exceptions.TelegramRetryAfter as flood_error:
            await asyncio.sleep(flood_error.retry_after)
            flood = True
        finally:
            if flood:
                return await send_message(user_id, message)
            return success

    successfully_sent = 0
    for user in all_users_id:
        sent = await send_message(user, sending_message)
        if sent:
            successfully_sent += 1
        await asyncio.sleep(sleep)
    return successfully_sent
