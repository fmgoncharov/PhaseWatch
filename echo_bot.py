import telebot
import os

bot = telebot.TeleBot(os.environ["BOT_TOKEN"])


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    return bot.reply_to(message, "Напиши мне размеры картинки через пробел. \n Например, 400 400")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        sizes = message.text.split()
        return bot.send_photo(message.chat.id, 'https://picsum.photos/' + sizes[0] + '/' + sizes[1])
    except:
        return bot.reply_to(message, "Неправильный формат. Попробуй ещё раз")


bot.infinity_polling()
