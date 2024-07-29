from aiogram import Bot
from aiogram.utils.keyboard import InlineKeyboardBuilder

async def channels_btn(channels, user_id, bot: Bot):
    markup = InlineKeyboardBuilder()
    for index, channel in enumerate(channels, start=1):
        channel = await bot.get_chat(channel)
        markup.button(text=f"{index}-kanal", url="https://T.me/" + channel.username)
    markup.button(text="✔ Tekshirish", callback_data=f"checksub")
    markup.adjust(1)
    return markup.as_markup()

async def help_message_btn(user_id, message_id):
    markup = InlineKeyboardBuilder()
    markup.button(text="Javob yozish", callback_data=f"help:{user_id}:{message_id}")
    return markup.as_markup()

async def channels_list_btn(channels, bot: Bot):
    markup = InlineKeyboardBuilder()
    for index, channel in enumerate(channels, start=1):
        try:
            channel = await bot.get_chat(channel[0])
            print(channel.username)
            markup.button(text=f"{index}-kanal", url="https://T.me/" + channel.username)
            markup.button(text=f"❌", callback_data=f"delChannel:{channel.id}")
        except: continue    
    markup.adjust(2)
    return markup.as_markup()

def withdraw_btn(user_id):
     markup = InlineKeyboardBuilder()
     markup.button(text="💰 Notcoinni yechib olish", callback_data=f"withdraw:{user_id}")
     return markup.as_markup()