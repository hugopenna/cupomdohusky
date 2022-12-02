import datetime
import sqlite3

import telebot
from decouple import config

bot = telebot.TeleBot(config('TOKEN'))
DB = 'main.db'
MSG_APOIO = ["""Tem sido divertido fazer esse bot.
Se te ajudei de alguma forma, 
considere me apoiar :)

CHAVE PIX:""", "26f2cc7b-5c72-4319-a0f6-a75ddbdf0dc3"]


@bot.message_handler(commands=["give"])
def cmd_give(message):
    print(message)
    msg = bot.send_message(message.chat.id, "mande seu cupom")
    bot.register_next_step_handler(msg, save_cupom)


def save_cupom(message):
    if len(message.text) != 12:
        msg = ['Eita, parece que isso não é um cupom.']
    else:
        msg = ["""seu cupom foi salvo com sucesso,
obrigado :)""", MSG_APOIO[0], MSG_APOIO[1]]

        con = sqlite3.connect(DB)
        cur = con.cursor()
        cur.execute("INSERT INTO cupons (cupom_id, given_by, given_date) VALUES (?,?,?);",
                    (message.text, message.from_user.id, datetime.date.today()))
        con.commit()

    for i in msg:
        bot.send_message(message.chat.id, i)
    print(message)
    print(msg)


@bot.message_handler(commands=["take"])
def cmd_take(message):
    prazo = datetime.date.today() - datetime.timedelta(days=30)

    con = sqlite3.connect(DB)
    cur = con.cursor()
    taker_valid = cur.execute("SELECT * from cupons WHERE taken_by=? AND taken_date>? ;", (message.from_user.id, prazo))
    taker_valid = taker_valid.fetchall()

    if len(taker_valid) >= 3:
        msg = ["Parece que vc já pegou cupons recentemente, vamos deixar para os outros amiguinhos também."]
    else:
        res = cur.execute("SELECT cupom_id FROM cupons WHERE taken_by IS NULL;")
        cupom = res.fetchone()

        if cupom is not None:
            msg = ["Pega esse cupom ae!", cupom[0], MSG_APOIO[0], MSG_APOIO[1]]
            cur.execute("UPDATE cupons SET taken_by=? , taken_date=? WHERE cupom_id=?;",
                        (message.from_user.id, datetime.date.today(), cupom[0]))
            con.commit()
        else:
            msg = ["Opa, parece que nao temos nenhum cupom no momento."]

    for i in msg:
        bot.send_message(message.chat.id, i)
    print(message)
    print(msg)


@bot.message_handler(commands=["apoiar"])
def cmd_apoiar(message):
    msg = MSG_APOIO

    for i in msg:
        bot.send_message(message.chat.id, i)


@bot.message_handler(func=lambda m: True)
def text(message):
    welcome_msg = """
    Bot para oferecer e pegar cupom do Husky.io
    Para comecar escolha um comando:
        /give - se quiser fornecer um cupom
        /take - se estiver precisando de um cupom
        /apoiar - para apoiar o desenvolvimento desse bot
        
    se precisar de ajuda chama o @hugopenna
    """
    bot.reply_to(message, welcome_msg)


bot.polling()
