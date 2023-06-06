from email import message
import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.token)



#@bot.message_handler(content_types=['text'])
#def echo(message):
#    bot.send_message(message.chat.id, message.text)





@bot.message_handler(commands = ['start'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text='Cайт', url='https://vk.com/')
    markup.add(btn)
    bot.send_message(message.from_user.id, "По этой кнопке ты перейдешь в vk", reply_markup = markup)


@bot.message_handler(content_types=['text'])
def mes(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn1 = types.KeyboardButton('Хорошо')
    
    btn2 = types.KeyboardButton('Не очень')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, 'Лень придумывать', reply_markup=markup)

    if message.text == 'Хорошо':
       bot.send_message(message.from_user.id, 'Это хорошо,  ' + '[ссылке](https://habr.com/ru/docs/help/rules/)', parse_mode='Markdown')
        



bot.polling(none_stop = True)