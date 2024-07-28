from aiogram import Router
from . import users
from . import admins

router = Router()

router.include_router(admins.router)
router.include_router(users.router)