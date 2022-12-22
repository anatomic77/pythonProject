import telebot
from telebot import types

bot = telebot.TeleBot('5979503402:AAG1s3diUHxkpWzRcjOwSbHLQtv2Cj4JEGE')

name = ''
surname = ''
bussines = ''
phone = ''


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, 'Здравствуйте! Пройдите пожалйста регистрацию введите /reg')


@bot.message_handler(func=lambda m: True)
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, 'Введете имя!')
        bot.register_next_step_handler(message, reg_name)


def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Введете фамлию!')
    bot.register_next_step_handler(message, reg_surname)


def reg_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Введете бизнес!')
    bot.register_next_step_handler(message, reg_bussines)


def reg_bussines(message):
    global bussines
    bussines = message.text
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='da', callback_data='yes')
    key_no = types.InlineKeyboardButton(text='net', callback_data='no')
    keyboard.add(key_yes, key_no)
    bot.send_message(message.from_user.id, f'Имя: {name} '
                                           f'Фамилия: {surname} '
                                           f'Бизнес: {bussines}', reply_markup=keyboard)


def reg_phone(message):
    global phone
    phone = message.text
    bot.send_message(message.chat.id, 'Спасибо, перейдите в канал аналитики!')


def question(message):
    bot.send_message(message.chat.id, 'эгорит')


@bot.callback_query_handler(func=lambda c: True)
def callback_worker(call):
    if call.data == 'no':
        bot.send_message(call.message.chat.id, 'пройдите регистрацию еще раз')
        bot.send_message(call.message.chat.id, 'Введите имя!')
        bot.register_next_step_handler(call.message, reg_name)
    elif call.data == 'yes':
        keyb2 = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton(text='konechno', callback_data='qq')
        item2 = types.InlineKeyboardButton(text='ne', callback_data='ww')
        keyb2.add(item1, item2)
        bot.send_message(call.message.chat.id, 'Хотлети бы разобрать на стриММе?', reply_markup=keyb2)
    elif call.data == 'qq':
        keyb3 = types.InlineKeyboardMarkup()
        item3 = types.InlineKeyboardButton(text='Горит', callback_data='it3')
        item4 = types.InlineKeyboardButton(text='все норм', callback_data='it4')
        keyb3.add(item3, item4)
        bot.send_message(call.message.chat.id, 'какая ситуация у вас в бизнесе?', reply_markup=keyb3)
        bot.register_next_step_handler(call.message, question)
    elif call.data == 'ww':
        keyb3 = types.InlineKeyboardMarkup()
        item3 = types.InlineKeyboardButton(text='Горит', callback_data='it3')
        item4 = types.InlineKeyboardButton(text='все норм', callback_data='it4')
        keyb3.add(item3, item4)
        bot.send_message(call.message.chat.id, 'какая ситуация у вас в бизнесе?', reply_markup=keyb3)
        bot.register_next_step_handler(call.message, question)
    elif call.data == 'it4':
        bot.register_next_step_handler(call.message, reg_phone)
        bot.send_message(call.message.chat.id, 'поделитесь вашим телефоном')


bot.polling()
