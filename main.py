from decouple import config
from Handlers import Handlers
from telegram.ext import Updater, CommandHandler
import logging

# set logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# instantiate bot
updater = Updater(
    token=config('TOKEN'),
    use_context=True
)
dispatcher = updater.dispatcher

# handler for start command
start_handler = CommandHandler('start', Handlers.start_handler)
dispatcher.add_handler(start_handler)

# Start Graphics
print("####################################")
print("####                            ####")
print("####      UniVrInfoArchive      ####")
print("####            Bot             ####")
print("####                            ####")
print("####################################\n")

# start bot
updater.start_polling()


