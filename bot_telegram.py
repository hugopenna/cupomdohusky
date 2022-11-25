import telebot

TOKEN = "5426919180:AAEyGzMQfGSjBwFZglCX04mm7jiuM9R_1Vg"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["give"])
def give_cupom(message):
    print(message)
    bot.reply_to(message, "mande seu cupom")

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