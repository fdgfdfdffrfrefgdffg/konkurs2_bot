from aiogram import Bot
from aiogram.types import CallbackQuery, FSInputFile, ReplyKeyboardRemove
from aiogram.enums import ChatMemberStatus
from aiogram.fsm.context import FSMContext
from bot_config  import ADMIN
import keyboards.inline as iBtns
import keyboards.reply as rBtns
import states.users as user_state
import data

async def answer_check_sub_channel(call: CallbackQuery, bot: Bot, state: FSMContext):
    not_sub_channels = []
    for channel in data.get_channels():
        status = await bot.get_chat_member(channel[0], call.from_user.id)
        status = status.status
        if not (status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.CREATOR, ChatMemberStatus.MEMBER, ChatMemberStatus.RESTRICTED]):
            not_sub_channels.append(channel[0])
    if not_sub_channels:
        markup = await iBtns.channels_btn(not_sub_channels, call.from_user.id, bot)
        await call.answer("Iltimos, quydagi kanallarga obuna bo'ling.", reply_markup=markup)
    else:
        user = data.get_user(call.from_user.id)
        if not user:
            await call.message.answer_animation(FSInputFile("animations/notcoin.gif"), caption="<b>Assalomu alaykum, NotCoin konkurs botga xush kelibsiz!</b>\n\nBotdan foydalanish uchun avval ro'yhatdan o'ting va ✅ Vazifa tugmasiga bosib, vazifangiz bilan tanishing hamda NotCoin yig'ishni boshlang.\n\n<b>Keling tanishib olamiz. Ismingiz?</b>", parse_mode="HTML", reply_markup=ReplyKeyboardRemove())
            await state.set_state(user_state.RegisterState.name)
        else:
            await call.answer("✅ Qabul qilindi!", show_alert=True)
            data.change_status_user(user.id, 1)
            data.change_status_ref(user.id, 1)
            await call.message.answer("Asosiy menyudasiz!", reply_markup=rBtns.main_menu_users)
    await call.message.delete()

async def answer_withdraw(call: CallbackQuery, bot: Bot):
    user_id = int(call.data.split(":")[1])
    ref_count = len(data.get_ref_count(user_id))
    if ref_count >= 20: 
        user = data.get_user(user_id)
        await bot.send_message(ADMIN, f"❗ {user.name} yetarli miqdorda Notcoin yig'di!\n\nBalans: {ref_count} Notcoin\nTelefon raqam: {user.phone}")
        await call.answer("'✅ Siz haqingizda adminga xabar qilindi. Tez orada sizga aloqaga chiqishadi.", show_alert=True)
    else:
        await call.answer(f"Siz hali {ref_count} Notcoin yig'gansiz! Kamida 20 ta Notcoin yig'ishingiz kerak!", show_alert=True)

