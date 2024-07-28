from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import keyboards.reply as rBtns
import data
import states.admins as admin_state
import utils

async def answer_sent(message: Message, state: FSMContext):
    await message.answer("Menga yubormoqchi bo'lgan xabaringizni yuboring,\n\nXabarda 1 tadan ortiq rasm yoki shunga o'xshash fayllar bo'lmasin.", reply_markup=rBtns.cancel_menu)
    await state.set_state(admin_state.SentMessageState.message)

async def answer_sent_message(message: Message, state: FSMContext):
    users = data.get_users()
    users_lst = [i[0] for i in users]
    
    sent_users_count = await utils.send_message_to_users(users_lst, message)
    await message.answer(
        f"✅ Topshiriq yakunlandi!\n\nMuvaffaqiyatli: {sent_users_count} ta\nMuvaffaqiyatsiz: {len(users) - sent_users_count} ta",
        reply_markup=rBtns.admin_menu
    )
    await state.clear()