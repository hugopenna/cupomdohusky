import telebot
from decouple import config
import sqlite3

bot = telebot.TeleBot('251487216:AAFZhGaBS_KEGLABlbyFeOVGzClIeSXQTRo')
con = sqlite3.connect('main.db')
cur = con.cursor()

cupons = ['30C37F3016B8', 'AB8015E7FC32', '11236EDF4236', 'FFC0A68DC165', '0A13A68C0291', 'DFAA143C409F',
          '2F95F410E869', '236F06462E95', 'D4D79B0593A3']


@bot.message_handler(commands=["take"])
def cmd_take(message):
    if cupons == []:
        msg = "Opa, parece que nao temos nenhum cupom no momento."
    else:
        msg = """Pega esse cupom ae!
{}""".format(cupons.pop(0))

    bot.send_message(message.chat.id, msg)
    print(message)
    print(cupons)


@bot.message_handler(commands=["give"])
def cmd_give(message):
    print(message)
    msg = bot.send_message(message.chat.id, "mande seu cupom")
    bot.register_next_step_handler(msg, save_cupom)


def save_cupom(message):
    cupons.append(message.text)
    print(cupons)
    bot.send_message(message.chat.id, """seu cupom foi salvo com sucesso, 
obrigado :)""")

    cur.execute("INSERT INTO cupons (cupom_id, given_by) VALUES (message.text, message.from_user.id);")
    con.commit()


@bot.message_handler(func=lambda m: True)
def text(message):
    WELCOME_MSG = """
    Bot para oferecer e pegar cupom do Husk.io
    Para comecar escolha um comando:
        /give - se quiser fornecer um cupom
        /take - se estiver precisando de um cupom
    """
    bot.reply_to(message, WELCOME_MSG)


bot.polling()
