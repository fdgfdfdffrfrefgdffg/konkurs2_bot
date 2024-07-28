from aiogram import Bot
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
import keyboards.inline as iBtns
import keyboards.reply as rBtns
import states
import data


async def answer_del_channel(call: CallbackQuery, bot: Bot):
    channel_id = call.data.split(":")[1]
    data.del_channel(int(channel_id))
    await call.answer("✅ Kanal o'chirildi!", show_alert=True)
    await call.message.delete()
    channels = data.get_channels()
    if channels:
        btn = await iBtns.channels_list_btn(channels, bot)
        await call.message.answer("Kanallar ro'yhati:", reply_markup=btn)
        await call.message.answer("Yana kanal qo'shamizmi?", reply_markup=rBtns.add_channel_btn)
    else: await call.message.answer("Kanallar mavjud emas!", reply_markup=rBtns.add_channel_btn)

async def reply_user_message(call: CallbackQuery, state: FSMContext):
    user_id = call.data.split(":")[1]
    message_id = call.data.split(":")[2]
    
    await state.update_data(user_id=user_id, message_id=message_id)
    await call.message.answer(f"Men tayyorman. Xabarni yuboring. Bekor qilish uchun bekor qilish tugmasiga bosing.", reply_markup=rBtns.cancel_menu)
    await state.set_state(states.admins.ReplyUserMessage.message)
