from aiogram.fsm.state import State, StatesGroup

class AddChannelState(StatesGroup):
    message = State()

class SentMessageState(StatesGroup):
    message = State()

class ReplyUserMessage(StatesGroup):
    message = State()
    