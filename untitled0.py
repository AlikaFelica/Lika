# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yZFYxlZpVdgz3lOhahSodEBvJd2FWyGc
"""

from google.colab import drive
drive.mount('/content/drive')

cd /content/drive/My Drive/Colab Notebooks

# pip install pyTelegramBotAPI
import telebot
from telebot import types

token = "5399763635:AAGZEBdD2ztYB4zrbxfq8XdYL2PTlJTR190"

bot = telebot.TeleBot(token, parse_mode = 'html')

# Обрабатываем команду /start
@bot.message_handler(commands=['start'])
def start(message):
   m = f'Привет, <b> {message.from_user.first_name} </b>'
   bot.send_message(message.chat.id, m, parse_mode='html')  

# Обрабатываем команду /help и создаем постоянные кнопки в окне снизу чата с ботом
@bot.message_handler(commands = ['help'])
def display_buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    scratch = types.KeyboardButton('Ролик Scratch')
    website = types.KeyboardButton('Веб-сайт проекта')
    facts = types.KeyboardButton('Факты об Аральском море')
    about_us = types.KeyboardButton('О нас')
    tracker = types.KeyboardButton('Бесплатный трекер эко-привычек')
    markup.add(scratch, website, about_us, facts, tracker )
    bot.send_message(message.chat.id, "Здесь ты можешь найти всю информацию", reply_markup=markup)

# Обрабатываем команды, когда пользователь присылает боту картинку
@bot.message_handler(content_types=['photo'])
def get_photo_from_user(message):
    bot.send_message(message.chat.id, "Ух ты, какое красивое фото!")

# Обрабатываем текст, приходящий от пользователя
@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text.lower() == "hello":
        bot.send_message(message.chat.id, "Добро пожаловать в Central Asia Water!", parse_mode = 'html')
        
    # При вводе текста photo, бот подгружает из папки картинку под названием '1617450766.jpg',
    # сохраняет ее в переменную photo и отправляет пользователю как ответ
    # ВНИМАНИЕ: чтобы эта часть кода работала, надо, чтобы и этот файл с кодом, и картинка, находились в одной папке
    elif message.text.lower() == "бесплатный трекер эко-привычек":
        photo = open('Central asia water.png', 'rb')
        bot.send_photo(message.chat.id, photo, parse_mode = 'html')   

    elif message.text.lower() == "факты об аральском море" :
       c1 = "1. Название Аральского моря происходит из местного диалекта, который в переводе буквально означает - море островов🌏."
       c2 = "2. До начала снижения уровня воды Аральское море находилось на 4-м месте, в списке крупнейших озер на планете - около 68 000 км."
       c3 = "3. В 2003г. Южное Аральское море разделилось на западную и восточную части."
       c4 = "4. Усыхание моря привело к изменениям местного климата: 🌅лето стало более сухим и жарким, а ⛄зима - более долгой и холодной."
       c5 = "5. Гладь моря - это растворенный ультрамарин. Такие синие воды 🌊 встречаются крайне редко. Не удивительно, что в русских документах Арал именовался Синим морем."
       text1 = c1
       text2 = c2
       text3 = c3
       text4 = c4
       text5 = c5
       bot.send_message(message.chat.id, text1 ) 
       bot.send_message(message.chat.id, text2 )
       bot.send_message(message.chat.id, text3 )
       bot.send_message(message.chat.id, text4 )
       bot.send_message(message.chat.id, text5 )
  
    # При нажатии на кнопку 'Ролик Scratch' это трансформируется в текст, и в ответ бот присылает в чат окно с ссылкой на сайт Scratch
    elif message.text.lower() == "ролик scratch":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(text='Scratch', url="https://scratch.mit.edu/projects/683683827") )
        bot.send_message(message.chat.id, "ролик в Scratch", reply_markup=markup)


    # При нажатии на кнопку 'Веб-сайт проекта' это трансформируется в текст, и в ответ бот присылает в чат окно с ссылкой на сайт Glith
    elif message.text.lower() == "веб-сайт проекта":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(text='Glitch', url="https://horse-broken-kick.glitch.me") )
        bot.send_message(message.chat.id, "Веб-сайт проекта", reply_markup=markup)   

         # При нажатии на кнопку 'О нас' это трансформируется в текст, 
    elif message.text.lower() == "о нас" :
        c3 = "Наш проект направлен на информирование жителей стран Центральной Азии о проблемах водных ресурсов."
        c4 = " Разработчиками проекта являются:  "
        c5 = "Бегимай: Добрый день! Меня зовут Акбарова Бегимай:) Я увлекаюсь волонтерством больше года. Я очень универсальный человек 🌈 я как приправа, что дополняет любую еду. На данный момент мне 16 лет, обучаюсь в 10 классе."
        c6 = "Адина: Всем привет! Мену зовут Баязитова Адина и мне 16, я занимаюсь проектами и научными работами обожаю книги и создавать!"
        c7 = "Малика: Приветствую всех, меня зовут Асылбекова Малика и мне 17. Я ученица НИШ ФМН г.Семей. Увлекаюсь дебатами, волонтерством и программированием!"
        text1 = c3 + c4
        text2 = c5
        text3 = c6
        text4 = c7
        bot.send_message(message.chat.id, text1)
        bot.send_message(message.chat.id, text2)
        bot.send_message(message.chat.id, text3)
        bot.send_message(message.chat.id, text4)

    else:
      bot.send_message(message.chat.id,"Я тебя не понимаю",parse_mode = 'html')
      
bot.polling(none_stop=True)

pip install pyTelegramBotAPI