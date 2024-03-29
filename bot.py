
# import datetime
# import sqlite3

import telebot
from decouple import config
from telebot import types
from telebot.util import quick_markup

import utils.msg as msg

bot = telebot.TeleBot(config('TOKEN'))
# DB = config('DB')
cupons = []


@bot.callback_query_handler(func=lambda q: q.data == 'give')
def qry_take(query):
    give_handler(query)

@bot.message_handler(commands=["give"])
def cmd_give(message):
    print(message)
    if message.chat.id < 0:
        button = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton(msg.btn_give,
                                         url=f'https://t.me/jamesbbot?start=give')
        button.add(btn, row_width=1)
        bot.reply_to(message, msg.give_cupom_grp, parse_mode='HTML', reply_markup=button)
    else:
        give_handler(message)

def give_handler(message):
    aux = bot.send_message(message.from_user.id, msg.send_cupom, parse_mode='markdownV2')
    bot.register_next_step_handler(aux, save_cupom)


def save_cupom(message):
    print(message)

    if len(message.text) != 12:
        bot.send_message(message.chat.id, msg.not_cupom, parse_mode='markdownV2')
        cmd_give(message)
        print(msg.not_cupom)
    else:
        cupons.append(message.text)
        bot.send_message(message.chat.id, msg.saved_cupom, parse_mode='markdownV2')
        print(msg.saved_cupom)




@bot.callback_query_handler(func=lambda q: q.data == 'take')
def qry_take(query):
    send_cupom(query)


@bot.message_handler(commands=["take"])
def cmd_take(message):
    print(message)
    if message.chat.id < 0:
        button = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton(msg.btn_take,
                                         url=f'https://t.me/jamesbbot?start=take')
        button.add(btn, row_width=1)
        bot.reply_to(message, msg.take_cupom, parse_mode='HTML', reply_markup=button)
    else:
        send_cupom(message)

def send_cupom(message):
    if len(cupons) != 0:
        aux = [msg.take_cupom, cupons[0], msg.disclaimer]
        cupons.pop(0)
    else:
        aux = [msg.without_cupom]

    for i in aux:
        bot.send_message(message.from_user.id, i, parse_mode='markdownV2')

    print(message)
    print(aux)


@bot.message_handler(commands=["stats"])
def cmd_stats(message):

    msg = "estamos trabalhando nisso"
    bot.send_message(message.from_user.id, msg)


@bot.message_handler(commands=["apoiar"])
def cmd_apoiar(message):
    bot.send_message(message.from_user.id, msg.apoio,
                     parse_mode='markdownV2')


@bot.message_handler(func=lambda m: True)
def text(message):

    if 'take' in message.text:
        send_cupom(message)
    elif 'give' in message.text:
        cmd_give(message)

    else:
        markup = quick_markup({'Pegar Cupom': {'callback_data': 'take'}, 'Deixar cupom': {'callback_data': 'give'}},
                              row_width=1)
        bot.reply_to(message, msg.welcome, parse_mode='markdownV2', reply_markup=markup)
    print(message)


bot.infinity_polling()
