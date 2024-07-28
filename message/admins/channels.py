from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Bot
import keyboards.inline as iBtns
import keyboards.reply as rBtns
import states.admins as admin_state
import data


async def answer_get_channels(message: Message, bot: Bot, state: FSMContext):
    channels = data.get_channels()
    if channels:
        btn = await iBtns.channels_list_btn(channels, bot)
        await message.answer("Kanallar ro'yhati:", reply_markup=btn)
        await message.answer("Yana kanal qo'shamizmi?", reply_markup=rBtns.add_channel_btn)
    else: await message.answer("Kanallar mavjud emas!", reply_markup=rBtns.add_channel_btn)

async def answer_add_channel(message: Message, bot: Bot, state: FSMContext):
    await message.answer("Menga kanaldan biror xabarni forward qiling.")
    await state.set_state(admin_state.AddChannelState.message)

async def answer_add_channel_message(message: Message, bot: Bot, state: FSMContext):
    if not message.forward_from_chat: await message.answer("Menga qo'shmoqchi bo'lgan kanalingizdan forward xabar yuboring.")
    else:
        try:
            chat_id = message.forward_from_chat.id
            chat = await bot.get_chat(chat_id=chat_id)
            data.add_channel(chat.id)
            await message.answer("✅ Kanal bazaga saqlandi!", reply_markup=rBtns.admin_menu)
            await state.clear()
        except:
            await message.answer("Kanal ma'lumotlarini olib bo'lmadi!")
            await message.answer("Menga qo'shmoqchi bo'lgan kanalingizdan forward xabar yuboring.")
