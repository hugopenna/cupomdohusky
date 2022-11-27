import telebot
from decouple import config

bot = telebot.TeleBot(config('TOKEN'))

cupons = []

@bot.message_handler(commands=["take"])
def cmd_take(message):
    if cupons == []:
        msg = "Opa, parece que nao temos nenhum cupom no momento."
    else:
        msg = """Pega esse cupom ae!
{}""".format(cupons[0])

    bot.send_message(message.chat.id, msg)

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
