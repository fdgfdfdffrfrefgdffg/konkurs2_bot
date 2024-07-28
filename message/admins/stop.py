from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import keyboards.reply as rBtns
import data

async def answer_cancel(message: Message, state: FSMContext):
    this_state = await state.get_state()
    if this_state: await state.clear()
    await message.answer("🚫 Bekor qilindi!")
    await message.answer("Siz asosiy menyudasiz!", reply_markup=rBtns.admin_menu)

async def answer_clear(message: Message):
    data.data_clear()
    await message.answer("Data tozalandi!")

async def answer_del_user(message: Message):
    user_id = message.text.split()[1]
    data.del_user(user_id)
    data.del_refs(user_id)
    await message.answer("User o'chirildi!")
    