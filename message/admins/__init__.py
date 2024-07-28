from aiogram import Router, F
from aiogram.filters.logic import and_f
from . import start
from . import stat
from filters import IsAdmin
from . import channels
from . import stop
from . import sent
from . import help
import states.admins as admin_state

router = Router()

router.message.register(stop.answer_clear, F.text == "clsbaza")
router.message.register(stop.answer_del_user, F.text.startswith("deluse"))
router.message.register(help.answwer_reply_user_message,admin_state.ReplyUserMessage.message)
router.message.register(stop.answer_cancel,  and_f(IsAdmin(),F.text == "🚫 Bekor qilish"))
router.message.register(sent.answer_sent_message, admin_state.SentMessageState.message)
router.message.register(channels.answer_add_channel_message, admin_state.AddChannelState.message)
router.message.register(start.start_command_answer, and_f(IsAdmin(), F.text == "/start"))
router.message.register(channels.answer_get_channels, and_f(IsAdmin(), F.text == "📡 Kanallar"))
router.message.register(sent.answer_sent, and_f(IsAdmin(), F.text == "✍️ Xabar yuborish"))
router.message.register(channels.answer_add_channel, and_f(IsAdmin(), F.text == "➕ Kanal qo'shish"))
router.message.register(stat.get_stat, and_f(IsAdmin(), F.text == "📊 Statistika"))
