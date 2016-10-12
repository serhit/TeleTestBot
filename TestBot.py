__author__ = 'serhit'

from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from datetime import datetime as dt

class Bot:
    def __init__(self, token):
        self.updater = Updater(token=token)

    def command(self, func):
        func_command = CommandHandler(func.__name__, func, pass_args = True)
        self.updater.dispatcher.add_handler(func_command)

        return func

    def text_message(self, func):
        func_command = MessageHandler([Filters.text], func)
        self.updater.dispatcher.add_handler(func_command)
        return func

    def cmd_message(self, func):
        func_command = MessageHandler([Filters.command], func)
        self.updater.dispatcher.add_handler(func_command)

    def run(self):
        self.updater.start_polling()

    def terminate(self):
        self.updater.stop()

mybot = Bot('296158453:AAHGuPwmoMm0Nxcw_ClijQPhwbDdzj2VXoc')

@mybot.command
def echo(bot, update, args):
    bot.sendMessage(chat_id = update.message.chat_id, text = ' '.join(args))

@mybot.command
def say(bot, update, args):
    bot.sendMessage(chat_id = update.message.chat_id, text = __name__)

@mybot.command
def time(bot, update, args):
    bot.sendMessage(chat_id = update.message.chat_id, text = str(dt.now()))

@mybot.cmd_message
def unknown(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text = 'I do not know this command')

@mybot.text_message
def chat(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text = 'Ok. I hear you. ' + update.message.text)


mybot.run()