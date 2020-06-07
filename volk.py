import logging
import volkcurr
import volkify
import volkifyParse

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Волк запущен. Волк уверен в себе.')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Волку не нужна помощь')


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def volk(update, context):
    data = volkcurr.get_currency_report()
    update.message.reply_text(data.desc)

def quote(update, context):
    html = volkifyParse.openHTML("https://socratify.net/quotes/random")

    print(volkify.volkify(volkifyParse.getPhrase(html), "волк"))
    print(volkify.volkify(volkifyParse.getAuthor(html), "волк"))

    quote = volkify.volkify(volkifyParse.getPhrase(html), "волк")
    author = volkify.volkify(volkifyParse.getAuthor(html), "волк")

    update.message.reply_text(quote)
    update.message.reply_text(author)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("volk", volk))
    dp.add_handler(CommandHandler("quote", quote))


    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

