bot_token = "6346817681:AAGaRprnqrN17gygtgUV7BGeJsXfl9TIBS4"

import telebot
from telebot import types
from notifiers import get_notifier

quea_list = ["ти і я", "він і вона", "воно і Даша"]
global i
i = 0

bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def start_function(message):
    bot.send_message(message.chat.id, "Привіт! \nЯ бот, який створений для того, щоб ви знали, хто чергує сьогодні")

@bot.message_handler(commands=['work'])
def work(message):
    markup = types.ReplyKeyboardMarkup()
    who = types.KeyboardButton("Хто черговий?")
    markup.add(who)
    bot.send_message(message.chat.id, "Працюю", reply_markup=markup)

@bot.message_handler(content_types="text")
def react_on_message(message):
    global i
    if message.text == "Хто черговий?":
        bot.send_message(message.chat.id, "Сьогодні чергові:\n" + quea_list[i])
        i += 1
        if i >= 3:
            i = 0   
bot.infinity_polling(none_stop= True)