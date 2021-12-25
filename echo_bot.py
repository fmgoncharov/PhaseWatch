import os

import telebot

bot = telebot.TeleBot(os.environ["BOT_TOKEN"])


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    return bot.reply_to(
        message, "Напишите мне размеры картинки через пробел. \nНапример, 2000 2000"
    )


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        sizes = message.text.split()
        if len(sizes) != 2:
            raise IndexError
        if not (sizes[0].isdecimal() and sizes[1].isdecimal()):
            raise SyntaxError
        if not (0 < int(sizes[0]) <= 5000 and 0 < int(sizes[1]) <= 5000):
            raise ValueError
        return bot.send_photo(
            message.chat.id, "https://picsum.photos/" + sizes[0] + "/" + sizes[1]
        )
    except IndexError:
        return bot.reply_to(message, "Неправильный формат. Введите ДВА числа")
    except SyntaxError:
        return bot.reply_to(message, "Неправильный формат. Введите два ЧИСЛА")
    except ValueError:
        return bot.reply_to(
            message, "Неправильный формат. Введите два числа из отрезка [1; 5000]"
        )


bot.infinity_polling()
