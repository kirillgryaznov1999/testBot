from email import message
import telebot
from telebot import types
import config
import requests


bot = telebot.TeleBot(config.token)
API_KEY = "your_api_key"
#@bot.message_handler(content_types=['text']) # Эхо бот
#def echo(message):
#    bot.send_message(message.chat.id, message.text)


@bot.message_handler(commands = ['start'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text='Cайт', url='https://vk.com/')
    markup.add(btn)
    bot.send_message(message.from_user.id, "По этой кнопке ты перейдешь в vk", reply_markup = markup)
    

@bot.message_handler(content_types=['text']) # Ссылка на заказ еды
def food(message):
    if message.text == "Хочу есть" or 'Голоден' or "Давай закажем еды":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Яндекс.Еда", url='https://eda.yandex.ru')
        btn2 = types.InlineKeyboardButton(text="DeliveryClub", url='https://www.delivery-club.ru/')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "Где хочешь заказать?", reply_markup = markup)

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
    


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот для показа погоды. Введи название города, погоду которого хочешь узнать.")

@bot.message_handler(func=lambda message: True)
def send_weather(message):
    city = message.text
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + API_KEY + "&units=metric")
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        message = "Погода в городе " + city.title() + ":\nТемпература: " + str(temp) + "°C\nОписание: " + description.title()
        bot.reply_to(message, message)
    else:
        bot.reply_to(message, "Произошла ошибка. Город не найден или API ключ неверный.")
        




bot.polling(none_stop = True)
