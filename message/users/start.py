from aiogram.types import Message, ReactionTypeCustomEmoji, ReplyKeyboardRemove,  FSInputFile
from aiogram.fsm.context import FSMContext
import keyboards.reply as btns
from aiogram.enums import ChatMemberStatus
import keyboards.inline as iBtns
import states.users as user_state
from bot_config import BOT_URL
from aiogram import Bot
import data

async def start_user(message: Message, state: FSMContext):
    user = data.get_user(message.from_user.id)
    if not user:
        await message.answer_animation(FSInputFile("animations/notcoin.gif"), caption="<b>Assalomu alaykum, Notcoin konkurs botga xush kelibsiz!</b>\n\nBotdan foydalanish uchun avval ro'yhatdan o'ting va ✅ Vazifa tugmasiga bosib, vazifangiz bilan tanishing hamda Notcoin yig'ishni boshlang.\n\n<b>Keling tanishib olamiz. Ismingiz?</b>", parse_mode="HTML", reply_markup=ReplyKeyboardRemove())
        await state.set_state(user_state.RegisterState.name)
    else:
        await message.answer("Asosiy menyudasiz!", reply_markup=btns.main_menu_users)

async def answer_name(message: Message, state: FSMContext):
    if len(message.text) > 70: await message.reply("Iltimos, ismingizni yozing.", reply_markup=ReplyKeyboardRemove())
    else:
        await message.reply(f"{message.text} tanishganimdan hursandman!")
        await message.reply("Endi menga telefon raqamingizni yuboring.", reply_markup=btns.sent_phone_btn)
        await state.update_data(name=message.text)
        await state.set_state(user_state.RegisterState.phone)

async def answer_phone(message: Message, bot: Bot, state: FSMContext):
    if (not message.contact) or message.contact.user_id != message.from_user.id or message.text:
        await message.answer("Pastdagi tugmaga bosib, telefon raqamingizni yuboring.", reply_markup=btns.sent_phone_btn)
        return
    
    if not (message.contact.phone_number.startswith("998") or message.contact.phone_number.startswith("+998")):
        await message.answer("Kechirasiz, sizni bloklashga majburman. Bu bot faqat o'zbek audiotoriyasi uchun ochilgan.")
        data.change_status_user(message.from_user.id, 0)
        return
    
    state_data = await state.get_data()
    data.add_user(message.from_user.id, state_data.get("name"), message.contact.phone_number)
    
    await message.answer(f"✔ Tabriklayman! Siz ro'yhatdan o'tdingiz!", reply_markup=btns.main_menu_users)
    reffer = data.get_reffer(message.from_user.id)
    if reffer:
        await bot.send_message(reffer[1], "Sizga 2 ta Notcoin qo'shildi!")
        data.change_status_ref(message.from_user.id, 1)
           
    await message.answer(f"Sizning taklif havolangiz:\n\n{BOT_URL}?start={message.from_user.id}")
    await state.clear()

async def start_ref_user(message: Message, bot: Bot, state: FSMContext):
    reffer_id = int(message.text[7:])
    user = data.get_user(message.from_user.id)
    reffer_user = data.get_user(reffer_id)
    is_referal = data.get_reffer_this_user(message.from_user.id)
    if user: 
        await message.reply("❗ Kechirasiz, siz referal bo'la olmaysiz! Sababi, siz oldin botdan ro'yhatdan o'tgansiz")
        return
    if is_referal: 
        await message.answer("❗ Siz referal bo'la olmaysiz! Sababi, avval referal bo'lgansiz!")
        return
    if not reffer_user: await message.answer("Do'stingiz bazada mavjud emas. Lekin, siz botdan foydalanishingiz mumkin.")
    else:
        await message.answer(f"Siz {reffer_user.name} do'stingiz tomonidan botga taklif qilindingiz!")
        await bot.send_message(reffer_id, "Hisobingizga 2 ta notcoin qo'shilishi mumkin. \n\nDo'stingiz to'liq ro'yhatdan o'tgach notcoin hisobingizga qo'shiladi!")
        data.add_ref(message.from_user.id, reffer_id)
        
    not_sub_channels = []
    for channel in data.get_channels():
        status = await bot.get_chat_member(channel[0], message.from_user.id)
        status = status.status
        if not (status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.CREATOR, ChatMemberStatus.MEMBER, ChatMemberStatus.RESTRICTED]):
            not_sub_channels.append(channel[0])
    if not_sub_channels:
        markup = await iBtns.channels_btn(not_sub_channels, message.from_user.id, bot)
        await message.answer("Iltimos, quydagi kanallarga obuna bo'ling.", reply_markup=markup)
    else:
        await message.answer_animation(FSInputFile("animations/notcoin.gif"), caption="<b>Assalomu alaykum, Notcoin konkurs botga xush kelibsiz!</b>\n\nBotdan foydalanish uchun avval ro'yhatdan o'ting va ✅ Vazifa tugmasiga bosib, vazifangiz bilan tanishing hamda Notcoin yig'ishni boshlang.\n\n<b>Keling tanishib olamiz. Ismingiz?</b>", parse_mode="HTML", reply_markup=ReplyKeyboardRemove())
        await state.set_state(user_state.RegisterState.name)

async def answer_not_sub_channels(message: Message, bot: Bot):
    not_sub_channels = []
    for channel in data.get_channels():
        status = await bot.get_chat_member(channel[0], message.from_user.id)
        status = status.status
        if not (status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.CREATOR, ChatMemberStatus.MEMBER, ChatMemberStatus.RESTRICTED]):
            not_sub_channels.append(channel[0])
    markup = await iBtns.channels_btn(not_sub_channels, message.from_user.id, bot)
    await message.answer("Iltimos, quydagi kanallarga obuna bo'ling.", reply_markup=markup)

async def aanswer_block_user(message: Message):
    pass