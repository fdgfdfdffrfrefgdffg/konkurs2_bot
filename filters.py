from aiogram import Bot
from aiogram.types import Message
from bot_config import ADMIN
from aiogram.enums import ChatMemberStatus
from aiogram.filters import Filter
import data

class IsRefUser(Filter):
    async def __call__(self, message: Message):
        if message.text:
            return "start " in message.text and message.text[7:].isdigit()
        return False

class IsSubDb(Filter):
    async def __call__(self, message: Message):
        user = data.get_user(message.from_user.id)
        if not user:
            return True
        return False

class IsAdmin(Filter):
    async def __call__(self, message: Message):
        return message.from_user.id == ADMIN

class IsSubChannels(Filter):
    async def __call__(self, message: Message, bot: Bot):
        not_sub_channels = []
        for channel in data.get_channels():
            status = await bot.get_chat_member(channel[0], message.from_user.id)
            status = status.status
            if not (status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.CREATOR, ChatMemberStatus.MEMBER, ChatMemberStatus.RESTRICTED]):
                not_sub_channels.append(channel[0])
        if not_sub_channels:
            return True
        return False

class IsBlockUser(Filter):
    async def __call__(self, message: Message):
        user = data.get_user(message.from_user.id)
        if user: return user.status == 0
        return False