from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import data
import keyboards.reply as rBtns
import states
import bot_config
import keyboards.inline as iBtn

async def answer_help(message: Message, state: FSMContext):
    await message.reply("Sizga qanday yordam berishim mumkin? Savolingizni bitta xabarda yozib yuboring.", reply_markup=rBtns.cancel_menu)
    await state.set_state(states.users.helpState.message)

async def answer_help_message(message: Message, bot: Bot, state: FSMContext):
    markup = await iBtn.help_message_btn(message.from_user.id, message.message_id)
    user = data.get_user(message.from_user.id)
    await bot.send_message(
        chat_id=bot_config.ADMIN,
        text=f"Foydalanuvchilardan xbaar:\n\nIsm-familya: {user.name}\nTelefon raqamL {user.phone}"
    )
    await message.copy_to(chat_id=bot_config.ADMIN, reply_markup=markup)
    await message.answer("✔ Xabar yetkazildi!", reply_markup=rBtns.main_menu_users)
    await state.clear()
