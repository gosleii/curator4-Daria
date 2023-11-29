import telebot

bot = telebot.TeleBot('6881696528:AAHlLiR8agBq430y1D541OFMGE973Z_AYns')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Добрый вечер!', parse_mode='Markdown')


@bot.message_handler(commands=['copy'])
def main(message):
    bot.send_message(message.chat.id, 'копировать пока нечего \nкопировать пока нечего', parse_mode='Markdown')


@bot.message_handler(commands=['bio'])
def main(message):
    bot.send_message(message.chat.id, 'ссылка на [САЙТ](https://vk.com/d.titova2)', parse_mode='Markdown')


@bot.message_handler(commands=['link'])
def main(message):
    bot.send_message(message.chat.id, '*куратор, улыбнись!*', parse_mode='Markdown')


bot.infinity_polling()