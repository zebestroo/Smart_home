import telebot
import datetime
import requests
from telebot import types # для указание типов

admins = [xxxxxxxxx, xxxxxxxxx, xxxxxxxxx, xxxxxxxxx] # Your admins telegram id's 
token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' # Token for tg Bot
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Управление домом")
    btn2 = types.KeyboardButton("❓ Узнать статус")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}, погнали рулить настройками дома!".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.from_user.id in admins):
        if(message.text == "❓ Узнать статус"):
            with open('logs.txt', 'r') as file:
                logs = file.read()
                bot.send_message(message.chat.id, text=logs)

        elif(message.text == "👋 Управление домом"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Полить теплицу")
            btn2 = types.KeyboardButton("Action2")
            back = types.KeyboardButton("Вернуться в главное меню")
            markup.add(btn1, btn2, back)
            bot.send_message(message.chat.id, text="Что будем делать?", reply_markup=markup)
        
        elif(message.text == "Полить теплицу"):
            r = requests.get(url = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
            if r:
                dt_now = datetime.datetime.now()
                dt_string = dt_now.strftime('%H:%M %d.%m.%Y')
                with open('logs.txt', 'w') as file:
                    file.write(f'Greenhouse was watered at {dt_string}\n')
                    file.write(f'Теплица поливалась в {dt_string}\n')

            bot.send_message(message.chat.id, text=f"Поливаю!")
            bot.send_message(message.chat.id, text=f"Что-нибудь ещё?")
        
        elif message.text == "Action2":
            bot.send_message(message.chat.id, text="Выполняю!")
        
        elif (message.text == "Вернуться в главное меню"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("👋 Управление домом")
            btn2 = types.KeyboardButton("❓ Узнать статус")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

        else:
            bot.send_message(message.chat.id, text="Sorry. Command not found:(")
    else:
        bot.send_message(message.chat.id, text="Sorry. There are privicy settings. You are not an admin...")


bot.polling(none_stop=True)
