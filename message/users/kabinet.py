from aiogram.types import Message, FSInputFile
from bot_config import BOT_URL
import data
import keyboards.inline as iBtns

async def answer_task(message: Message):

    post_text = f"""
❗️ <b>BEPUL NOTCOIN TARQATILYAPTI</b>

 <b>Shartlar juda oddiy:</b>
  - Do'stingiz bergan havola orqali botga tashrif buyuring.
  - Kanallarga obuna bo'ling.
  - Botdan ro'yhatdan o'ting
  - Vazifalar bajarib Notcoin yig'ing va yig'ilgan Notcoinni pulga almashtiring.

👇<b> Quydagi havola orqali botga tashrif buyuring.</b>
{BOT_URL}?start={message.from_user.id}
"""
    image_path = "animations/post.jpg"
    await message.answer_photo(photo=FSInputFile(image_path), caption=post_text, parse_mode="HTML")

    text = f"✅ Vazifa:\n\n"
    text += "Ushbu postni do'stlaringizga va guruhlarga ulashing va har bir do'stingiz uchun 1 dona Notcoin qo'lga kiriting!" 
    await message.answer(text)

async def answer_balans(message: Message):
    balans = len(data.get_ref_count(message.from_user.id))
    user = data.get_user(message.from_user.id)
    text = F"SIZNING MA'LUMOTLARINGIZ:\n\nIsm-familya: {user.name}\nBalans: {balans} Notcoin\nTelefon raqam: {user.phone}\n\n1 Notcoin - 500 UZS"
    await message.answer(text, reply_markup=iBtns.withdraw_btn(message.from_user.id))
