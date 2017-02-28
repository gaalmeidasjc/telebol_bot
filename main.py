import telegram
from converte import converte
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

#Conectando a API do Telegram
updater = Updater(token="326652376:AAGHzGef6TeR5J567XZNmO93ab2P_PWeNKg")
dispatcher = updater.dispatcher

def start(bot, update):
    me = bot.get_me()
    msg = "Teste start"

    bot.send_message(chat_id=update.message.chat_id,
                     text=msg)

def corinthians(bot,update):
    msg = converte("corinthians")
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg)

def unknown(bot, update):
    msg = "Comando invalido."
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg)

start_handler = CommandHandler("start", start)
help_handler = CommandHandler("help", start)
corinthians_handler = CommandHandler("corinthians",corinthians)
unknown_handler = MessageHandler((Filters.command),unknown)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(corinthians_handler)
dispatcher.add_handler(unknown_handler)
