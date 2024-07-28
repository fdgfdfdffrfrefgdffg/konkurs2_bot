from aiogram import Router, F
from . import users
from . import admins

router = Router()

router.callback_query.register(admins.reply_user_message, F.data.startswith("help"))
router.callback_query.register(users.answer_check_sub_channel, F.data == "checksub")
router.callback_query.register(users.answer_withdraw, F.data.startswith("withdraw"))
router.callback_query.register(admins.answer_del_channel, F.data.startswith("delChannel"))
