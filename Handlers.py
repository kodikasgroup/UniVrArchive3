from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from Utils import Utils
import telegram


class Handlers:
    @staticmethod
    def start_handler(update: Update, context: CallbackContext) -> None:
        """
        handle the command /start, it sends a gif, a welcome message and shows the
        buttons to access the archive
        :param update:
        :param context:
        :return:
        """
        chat_id = update.message.chat_id
        first_name = update.message.chat.first_name
        message = Utils.get_start_message(opening="Benvenuto/a", name=first_name)
        doc = open('resources/intro.gif', 'rb')
        buttons = Utils.get_start_buttons()
        reply_markup = InlineKeyboardMarkup(buttons)

        context.bot.send_photo(chat_id, doc)
        context.bot.send_message(chat_id=chat_id,
                                 text=message,
                                 parse_mode=telegram.ParseMode.MARKDOWN_V2,
                                 reply_markup=reply_markup)
