import telebot
from telebot import types
from TOKEN import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['left_chat_member'])
def handle_left_member(message):
    user_id = message.left_chat_member.id
    chat_id = message.chat.id
    user_name = message.left_chat_member.first_name

    try:
        bot.ban_chat_member(chat_id, user_id)
        bot.send_message(chat_id, f"Usuário {user_name} foi banido por sair do grupo.")
    except Exception as e:
        print(f"Erro ao tentar banir o usuário: {e}")
        bot.send_message(chat_id, "Houve um erro ao banir o usuário.")

bot.polling()
