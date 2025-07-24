import telebot

BOT_TOKEN = '8199489852:AAGR_0OcAQYRzKAM5tAgSIpux5j3wneyvto'
bot = telebot.TeleBot(BOT_TOKEN)

# Your code-to-video map
video_map = {
    "1": "BAACAgUAAxkBAAMKaIC3k9oG5Mj-qK1shxw9R9inCpIAAkAWAAIqtghUBE7T5Zouk742BA",  # Replace with real file_id
    "2": "BAACAgUAAxkBAAMNaIC3kzs932Fzk6fzq81kIhrJfykAAkUWAAIqtghUSzRE6-OQCSM2BA",
    "3": "BAACAgUAAxkBAAMMaIC3k6iv_iFQakoT5Mto1Ve9muEAAkQWAAIqtghU6yTZErEfeqI2BA"
}

@bot.message_handler(func=lambda msg: True)
def handle_code(message):
    code = message.text.strip()
    if code in video_map:
        bot.send_video(message.chat.id, video_map[code])
    else:
        bot.send_message(message.chat.id, "❌ Invalid code. Send 1, 2, or 3.")

bot.infinity_polling(timeout=10, long_polling_timeout=5)