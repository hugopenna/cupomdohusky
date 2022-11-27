import telebot

TOKEN = "5426919180:AAEyGzMQfGSjBwFZglCX04mm7jiuM9R_1Vg"

bot = telebot.TeleBot(TOKEN)

cupons = []


@bot.message_handler(commands=["give"])
def give_cupom(message):
    print(message)
    msg = bot.send_message(message.chat.id, "mande seu cupom")
    bot.register_next_step_handler(msg, save_cupom)


def save_cupom(message):
    cupons.append(message.text)
    print(cupons)
    msg = bot.send_message(message.chat.id, """seu cupom foi salvo com sucesso, 
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
