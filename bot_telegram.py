import telebot
from decouple import config
import sqlite3

bot = telebot.TeleBot(config('TOKEN'))


@bot.message_handler(commands=["give"])
def cmd_give(message):
    print(message)
    msg = bot.send_message(message.chat.id, "mande seu cupom")
    bot.register_next_step_handler(msg, save_cupom)


def save_cupom(message):
    if len(message.text) != 12:
        msg = 'Eita, parece que isso não é um cupom.'
    else:
        msg = """seu cupom foi salvo com sucesso,
obrigado :)"""

        con = sqlite3.connect('main.db')
        cur = con.cursor()
        cur.execute("INSERT INTO cupons (cupom_id, given_by) VALUES (?,?);", (message.text, message.from_user.id))
        con.commit()

    bot.send_message(message.chat.id, msg)
    cmd_apoiar(message)
    print(message)
    print(msg)


@bot.message_handler(commands=["take"])
def cmd_take(message):
    con = sqlite3.connect('main.db')
    cur = con.cursor()
    res = cur.execute("SELECT cupom_id FROM cupons WHERE taken_by IS NULL;")
    cupom = res.fetchone()

    if None != cupom:
        msg = """Pega esse cupom ae!
{}""".format(cupom[0])
        cur.execute("UPDATE cupons SET taken_by=? WHERE cupom_id=?;", (message.from_user.id, cupom[0]))
        con.commit()
    else:
        msg = "Opa, parece que nao temos nenhum cupom no momento."

    bot.send_message(message.chat.id, msg)
    cmd_apoiar(message)
    print(message)
    print(msg)


@bot.message_handler(commands=["apoiar"])
def cmd_apoiar(message):
    msg ="""Tem sido divertido fazer esse bot, 
se te ajudei de alguma forma, considere me apoiar.

CHAVE PIX:
26f2cc7b-5c72-4319-a0f6-a75ddbdf0dc3"""
    bot.send_message(message.chat.id, msg)

@bot.message_handler(func=lambda m: True)
def text(message):
    WELCOME_MSG = """
    Bot para oferecer e pegar cupom do Husk.io
    Para comecar escolha um comando:
        /give - se quiser fornecer um cupom
        /take - se estiver precisando de um cupom
        /apoiar - para apoiar o desenvolvimento desse bot
        
    se precisar de ajuda chama o @hugopenna
    """
    bot.reply_to(message, WELCOME_MSG)


bot.polling()
