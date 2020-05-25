
import telebot
import random
import os
from os import environ

bot = environ['TOKEN']




# bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Пора кидать кости!', reply_markup=keyboard)




keyboard = telebot.types.InlineKeyboardMarkup()
key_d2 = telebot.types.InlineKeyboardButton(text='d2', callback_data='d2')
keyboard.add(key_d2)
key_d3 = telebot.types.InlineKeyboardButton(text='d3', callback_data='d3')
keyboard.add(key_d3)
key_d4 = telebot.types.InlineKeyboardButton(text='d4', callback_data='d4')
keyboard.add(key_d4)
key_d6 = telebot.types.InlineKeyboardButton(text='d6', callback_data='d6')
keyboard.add(key_d6)
key_d8 = telebot.types.InlineKeyboardButton(text='d8', callback_data='d8')
keyboard.add(key_d8)
key_d10 = telebot.types.InlineKeyboardButton(text='d10', callback_data='d10')
keyboard.add(key_d10)
key_d12 = telebot.types.InlineKeyboardButton(text='d12', callback_data='d12')
keyboard.add(key_d12)
key_d20 = telebot.types.InlineKeyboardButton(text='d20', callback_data='d20')
keyboard.add(key_d20)
key_d100 = telebot.types.InlineKeyboardButton(text='d100', callback_data='d100')
keyboard.add(key_d100)

@bot.callback_query_handler(func=lambda call : True)

def callback(call):
    if call.data == 'd2':
        msg = f'Ваш результат: {roll_dice("d2")}'
        bot.send_message(call.message.chat.id, msg,reply_markup=keyboard)
    elif call.data == 'd3':
        msg =f'Ваш результат: {roll_dice("d3")}'
        bot.send_message(call.message.chat.id, msg,reply_markup=keyboard)
    elif call.data == 'd4':
        msg =f'Ваш результат: {roll_dice("d4")}'
        bot.send_message(call.message.chat.id, msg,reply_markup=keyboard)
    elif call.data == 'd6':
        msg =f'Ваш результат: {roll_dice("d6")}'
        bot.send_message(call.message.chat.id, msg,reply_markup=keyboard)
    elif call.data == 'd8':
        msg =f'Ваш результат: {roll_dice("d8")}'
        bot.send_message(call.message.chat.id, msg,reply_markup=keyboard)
    elif call.data == 'd10':
        msg =f'Ваш результат: {roll_dice("d10")}'
        bot.send_message(call.message.chat.id, msg,reply_markup=keyboard)
    elif call.data == 'd12':
        msg =f'Ваш результат: {roll_dice("d12")}'
        bot.send_message(call.message.chat.id, msg,reply_markup=keyboard)
    elif call.data == 'd20':
        msg =f'Ваш результат: {roll_dice("d20")}'
        bot.send_message(call.message.chat.id, msg,reply_markup=keyboard)
    elif call.data == 'd100':
        msg =f'Ваш результат: {roll_dice("d100")}'
        bot.send_message(call.message.chat.id, msg,reply_markup=keyboard)


def roll_dice(button):
    if button == 'd2':
        return random.randint(1,2)
    elif button == 'd3':
        return random.randint(1, 3)
    elif button == 'd4':
        return random.randint(1, 4)
    elif button == 'd6':
        return random.randint(1, 6)
    elif button == 'd8':
        return random.randint(1, 8)
    elif button == 'd10':
        return random.randint(1, 10)
    elif button == 'd12':
        return random.randint(1, 12)
    elif button == 'd20':
        return random.randint(1, 20)
    elif button == 'd100':
        return random.randint(1, 100)


bot.polling()