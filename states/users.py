from aiogram.fsm.state import State, StatesGroup

class RegisterState(StatesGroup):
    name = State()
    phone = State()

class helpState(StatesGroup):
    message = State()