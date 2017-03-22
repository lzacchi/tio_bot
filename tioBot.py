import logging

import os

import random

from jokes import jokes, respostas

import telegram


from telegram.ext import CommandHandler, Filters, MessageHandler, Updater


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='E aí rapaziada kkkk')


def trigger(percentage=10):
    return random.randrange(100) < percentage


def cmd_help(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='Molecada, o tio tá aqui pra divertir vocês. Mandem "/joke", que o tio manda uma piada ótima de chorar de rir mesmo. Só o bode riso kkkkk')


def joke(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=random.choice(jokes))


def replies(bot, update):
    if trigger():
        message = update.message
        if 'pave' in message.text.lower() or 'pavê' in message.text.lower():
            message.reply_text('é pavê ou pacomê?')
        if 'temer' in message.text.lower():
            message.reply_text('FORA TEMER \n ESSES POLÍTICO É TUDO SAFADO KKKKKK')

def rekt(bot, update):
    message = update.message
    if 'rekt' in message.text.lower():
        bot.sendMessage(chat_id=message.chat_id, text=random.choice(respostas))

token = os.environ.get('TOKEN')
appname = os.environ.get('APPNAME')
port = int(os.environ.get('PORT', '5000'))

updater = Updater(token)
updater.start_webhook(listen="0.0.0.0", port=port, url_path=token)
updater.bot.setWebhook("https://tio-bot.herokuapp.com/{}".format(token))
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
help_handler = CommandHandler('help@tioBot', cmd_help)
dispatcher.add_handler(help_handler)
joke_handler = CommandHandler('joke', joke)
dispatcher.add_handler(joke_handler)
dispatcher.add_handler(MessageHandler(Filters.all, replies))
updater.idle()
