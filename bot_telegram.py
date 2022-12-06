import datetime
import sqlite3

import telebot
from decouple import config
import utils.msg as msg

bot = telebot.TeleBot(config('TOKEN'))
DB = config('DB')


@bot.message_handler(commands=["give"])
def cmd_give(message):
    print(message)
    aux = bot.send_message(message.from_user.id, msg.send_cupom, parse_mode='markdownV2')
    bot.register_next_step_handler(aux, save_cupom)


def save_cupom(message):
    if len(message.text) != 12:
        aux = [msg.not_cupom]
    else:
        aux = [msg.saved_cupom]

        con = sqlite3.connect(DB)
        cur = con.cursor()
        cur.execute("INSERT INTO cupons (cupom_id, given_by, given_date) VALUES (?,?,?);",
                    (message.text, message.from_user.id, datetime.date.today()))
        con.commit()

    for i in aux:
        bot.send_message(message.chat.id, i, parse_mode='markdownV2')
    print(message)
    print(aux)


@bot.message_handler(commands=["take"])
def cmd_take(message):
    prazo = datetime.date.today() - datetime.timedelta(days=30)

    con = sqlite3.connect(DB)
    cur = con.cursor()
    taker_valid = cur.execute("SELECT * from cupons WHERE taken_by=? AND taken_date>? ;", (message.from_user.id, prazo))
    taker_valid = taker_valid.fetchall()

    if len(taker_valid) >= 3:
        aux = [msg.too_many_cupom]
    else:
        res = cur.execute("SELECT cupom_id FROM cupons WHERE taken_by IS NULL;")
        cupom = res.fetchone()

        if cupom is not None:
            aux = [msg.take_cupom, cupom[0], msg.disclaimer]
            cur.execute("UPDATE cupons SET taken_by=? , taken_date=? WHERE cupom_id=?;",
                        (message.from_user.id, datetime.date.today(), cupom[0]))
            con.commit()
        else:
            aux = [msg.without_cupom]

    for i in aux:
        bot.send_message(message.from_user.id, i, parse_mode='markdownV2')

    print(message)
    print(aux)


@bot.message_handler(commands=["apoiar"])
def cmd_apoiar(message):
    bot.send_message(message.from_user.id, msg.apoio,
                     parse_mode='markdownV2')


@bot.message_handler(func=lambda m: True)
def text(message):
    bot.reply_to(message, msg.welcome, parse_mode='markdownV2')


bot.polling()
