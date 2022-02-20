import constants
import telebot
from telebot import types

bot = telebot.TeleBot('2119464296:AAHHvLPvNioNKU58ucHa6cA1zeaHhsRUi18')


@bot.message_handler(commands=['hello'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет ,гость,для того,чтобы узнать больше о боте пропишите /help \r\nТак же если посмотреть что-то про место нашего обучения можешь прописать  /study')


@bot.message_handler(commands=['help'])
def help_mes(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btnDel = types.KeyboardButton('Что мы делаем')
    btnPrecol = types.KeyboardButton('Секретная кнопка')
    btnGif = types.KeyboardButton('Прикольная гифка')
    markup.add(btnDel)
    markup.add(btnPrecol)  
    markup.add(btnGif)      
    bot.send_message(message.chat.id, 'Выбери что ты хочешь узнать', reply_markup=markup)

@bot.message_handler(commands=['study'])
def study_mes(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btnSait = types.KeyboardButton('Сайт нашего универа')
    btnWho = types.KeyboardButton('Сайт кафедры')
    markup.add(btnSait)
    markup.add(btnWho)
    bot.send_message(message.chat.id, 'Выбери что ты хочешь узнать', reply_markup=markup)

@bot.message_handler(content_types='text')
def reply_message(message):
    if message.text == 'Что мы делаем':
        bot.send_message(message.chat.id, 'Учимся не покладая рук ,занимаемся саморазвитием и отдыхаем')
    if message.text == 'Секретная кнопка':
        bot.send_message(message.chat.id, constants.random_message())
    if message.text == 'Прикольная гифка':
        bot.send_video(message.chat.id, constants.random_message2())
    if message.text == 'Сайт нашего универа':
        bot.send_message(message.chat.id, 'https://mtuci.ru/')
    if message.text == 'Сайт кафедры':
        bot.send_message(message.chat.id, 'https://mtuci.tech/')



bot.infinity_polling()
