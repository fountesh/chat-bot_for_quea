bot_token = "Bot_Token"

import telebot
import time
from telebot import types
from notifiers import get_notifier

quea_list = ["a", "b", "c"]
global i
i = 0

bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def start_function(message):
    bot.send_message(message.chat.id, "Привіт! \nЯ бот, який створений для того, щоб ви знали, хто чергує сьогодні\nДля того щоб ввімкнути кнопки напишіть /work")

@bot.message_handler(commands=['work'])
def work(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    who = types.KeyboardButton("Обрати чергових")
    see = types.KeyboardButton("Дізнатися хто черговий")
    markup.add(who, see)
    bot.send_message(message.chat.id, "Працюю", reply_markup=markup,)

@bot.message_handler(content_types="text")
def react_on_message(message):
    global i
     
    if message.text == "Обрати чергових":
        markup_inline = types.InlineKeyboardMarkup()
        aggre = types.InlineKeyboardButton("✅", callback_data="Виходить")
        disagre = types.InlineKeyboardButton("❌", callback_data="Не виходить")
        markup_inline.add(aggre, disagre)
        bot.send_message(message.chat.id, "Сьогодні мають чергувати:\n" + quea_list[i] + "\nУ вас виходить?", reply_markup=markup_inline)
    if message.text == "Дізнатися хто черговий":
        bot.send_message(message.chat.id, "Сьогодні чергові:\n" + quea_list[i - 1])
    @bot.callback_query_handler(func=lambda call:True)
    def answer(call):
        global i
        if call.data == "Виходить":
            bot.send_message(call.message.chat.id, "Чергові:\n" + quea_list[i])
            i += 1
            if i >= 3:
                i = 0
        if call.data == "Не виходить":
            i += 1
            if i >= 3:
                i = 0
            bot.send_message(call.message.chat.id, "Тоді сьогодні чергові:\n" + quea_list[i], reply_markup=markup_inline)

bot.infinity_polling(none_stop= True)
