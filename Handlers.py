import logging
import traceback

import telegram
from telegram import Update, InlineKeyboardMarkup
from telegram.ext import CallbackContext

from ButtonGenerator import ButtonGenerator
from StartButtonHandler import StartButtonHandler
from Utils import Utils


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
        buttons = ButtonGenerator.get_start_buttons()
        reply_markup = InlineKeyboardMarkup(buttons)

        context.bot.send_photo(chat_id, doc)
        context.bot.send_message(chat_id=chat_id,
                                 text=message,
                                 parse_mode=telegram.ParseMode.MARKDOWN_V2,
                                 reply_markup=reply_markup)

    @staticmethod
    def inline_button_handler(update: Update, context: CallbackContext) -> None:
        """

        :param update:
        :param context:
        :return:
        """

        chat_id = update.callback_query.from_user.id
        text = update.callback_query.data
        if text == 'EXCLUSIVE':
            pass
        elif text == 'HOME':
            StartButtonHandler.home_button_handler(update, context)
        elif 'BACK' in text:
            StartButtonHandler.back_button_handler(update, context, text)
        else:
            if '_course' in text:
                StartButtonHandler.course_button_handler(context, text, chat_id)
            elif '__year' in text:
                StartButtonHandler.year_button_handler(update, context, text, chat_id)
            elif '__subject' in text:
                StartButtonHandler.subject_button_handler(update, context, text, chat_id)
            elif '__subdir' in text:
                StartButtonHandler.subdir_button_handler(update, context, text, chat_id)
            elif '__file' in text:
                StartButtonHandler.file_button_handler(update, context, text, chat_id)

    @staticmethod
    def error_handler(update: Update, context: CallbackContext):
        """
        Log the error and send a telegram message to notify the developer.
        :param update:
        :param context:
        :return:
        """
        logging.info("An Error Occurred: ")
        traceback.print_tb(context.error.__traceback__)
        message = "Ci dispiace😞😞" \
                  "\nSembra si sia verificato un'errore perfavore riavvia il bot utilizzando il comando \/start"
        context.bot.send_message(chat_id=update.callback_query.from_user.id,
                                 text=message,
                                 parse_mode=telegram.ParseMode.MARKDOWN_V2)
