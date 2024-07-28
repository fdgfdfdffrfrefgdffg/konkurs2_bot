from aiogram.utils.keyboard import ReplyKeyboardBuilder

sent_phone_btn = ReplyKeyboardBuilder()
sent_phone_btn.button(text="✔ Telefon raqamni yuborish uchun bosing", request_contact=True)
sent_phone_btn = sent_phone_btn.as_markup()
sent_phone_btn.resize_keyboard = True
sent_phone_btn.is_persistent = True

main_menu_users = ReplyKeyboardBuilder()
main_menu_users.button(text="✅ Vazifa")
main_menu_users.button(text="👤 Hisobim")
main_menu_users.button(text="🆘 Yordam")
main_menu_users.button(text="📊 Statistika")
main_menu_users.adjust(2)
main_menu_users = main_menu_users.as_markup()
main_menu_users.is_persistent = True
main_menu_users.resize_keyboard = True

admin_menu = ReplyKeyboardBuilder()
admin_menu.button(text="📡 Kanallar")
admin_menu.button(text="📊 Statistika")
admin_menu.button(text="✍️ Xabar yuborish")
admin_menu = admin_menu.as_markup()
admin_menu.resize_keyboard = True
admin_menu.is_persistent = True

add_channel_btn = ReplyKeyboardBuilder()
add_channel_btn.button(text="➕ Kanal qo'shish")
add_channel_btn.button(text="🚫 Bekor qilish")
add_channel_btn = add_channel_btn.as_markup()
add_channel_btn.resize_keyboard = True
add_channel_btn.is_persistent = True

cancel_menu = ReplyKeyboardBuilder()
cancel_menu.button(text="🚫 Bekor qilish")
cancel_menu = cancel_menu.as_markup()
cancel_menu.resize_keyboard = True
cancel_menu.is_persistent = True