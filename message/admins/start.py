from aiogram.types import Message
import keyboards.reply as rBtns

async def start_command_answer(message: Message):
    await message.answer("Assalomu alaykum, admin", reply_markup=rBtns.admin_menu)
