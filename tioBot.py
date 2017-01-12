import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random
import logging
from jokes import jokes
from configTio import TOKEN


import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def start(bot, update):
	bot.sendMessage(chat_id = update.message.chat_id, text = 'E aí rapaziada kkkk')


def cmd_help(bot, update):
	bot.sendMessage(chat_id = update.message.chat_id, text = 'Molecada, o tio tá aqui pra divertir vocês. Mandem "/joke", que o tio manda uma piada ótima de chorar de rir mesmo. Só o bode riso kkkkk')

def joke(bot, update):
	bot.sendMessage(chat_id = update.message.chat_id, text = random.choice(jokes))

def replies(bot, update):
	chat_id = update.message.chat_id
	message = update.message
	if 'pave' in message.text.lower() or 'pavê' in message.text.lower():
		message.reply_text('é pavê ou pacomê?')
	if 'temer' in message.text.lower():
		message.reply_text('FORA TEMER \n ESSES POLÍTICO É TUDO SAFADO KKKKKK')
	if 'livro' in message.text.lower():
		message.reply_text('Tá cu livrinho aí?')
	if 'cortar cabelo' in message.text.lower() or 'cortar meu cabelo' in message.text.lower() or 'cortar o cabelo' in message.text.lower():
		message.reply_text('Vai no cabelereiro? Quer corta a frente e pica atrás?')
	if 'tomar no cu' in message.text.lower():
		message.reply_text('Tomate cru é vitamina, como tu e tua prima!')
	if 'café' in message.text.lower() or 'cafe' in message.text.lower():
		message.reply_text('Prefere na cafeteira ou no cuador é mais forte?')
	if 'quente' in message.text.lower() or 'calor' in message.text.lower():
		message.reply_text('Nesse calor como sua a bunda né?')

updater = Updater (TOKEN)
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
help_handler = CommandHandler('help', cmd_help)
dispatcher.add_handler(help_handler)
joke_handler = CommandHandler('joke', joke)
dispatcher.add_handler(joke_handler)
dispatcher.add_handler(MessageHandler(Filters.all, replies))

updater.start_polling()
updater.idle()