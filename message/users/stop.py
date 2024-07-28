from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import keyboards.reply as rBtns

async def answer_cancel(message: Message, state: FSMContext):
    this_state = await state.get_state()
    if this_state: await state.clear()
    await message.answer("🚫 Bekor qilindi!")
    await message.answer("Siz asosiy menyudasiz!", reply_markup=rBtns.main_menu_users)
    