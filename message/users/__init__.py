from aiogram import Router, F
import filters
from aiogram.filters import CommandStart, and_f
from . import stat
from . import start
from . import help
from . import kabinet
from . import stop
import states

router = Router()

router.message.register(start.answer_name, states.users.RegisterState.name)
router.message.register(start.answer_phone, states.users.RegisterState.phone)
router.message.register(help.answer_help_message, states.users.helpState.message)
router.message.register(start.aanswer_block_user, filters.IsBlockUser())
router.message.register(start.start_ref_user, filters.IsRefUser())
router.message.register(stop.answer_cancel, F.text == "🚫 Bekor qilish")
router.message.register(start.answer_not_sub_channels, filters.IsSubChannels())
router.message.register(start.start_user, filters.IsSubDb())

router.message.register(start.start_user, F.text == "/start")
router.message.register(start.start_ref_user, filters.IsRefUser())
router.message.register(kabinet.answer_task, F.text == "✅ Vazifa")
router.message.register(help.answer_help, F.text == "🆘 Yordam")
router.message.register(kabinet.answer_balans, F.text == "👤 Hisobim")
router.message.register(stat.get_stat, F.text == "📊 Statistika")
