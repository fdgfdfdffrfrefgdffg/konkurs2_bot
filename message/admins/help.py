from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import keyboards.reply as rBtns
from aiogram import Bot

async def answwer_reply_user_message(message: Message, bot: Bot, state: FSMContext):
    data = await state.get_data()
    await bot.send_message(data.get("user_id"), text="❗ Bu xabarga admindan javob!",  reply_to_message_id=data.get("message_id"))    
    await message.copy_to(chat_id=data.get("user_id"))
    await message.answer("✅ Xabar yetkazildi!", reply_markup=rBtns.admin_menu)
    await state.clear()