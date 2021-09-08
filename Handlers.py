import os

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from Utils import Utils
import telegram


class Handlers:
    selected_course = ""
    selected_year = ""

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

    @staticmethod
    def _home_button_handler(update: Update, context: CallbackContext) -> None:
        """

        :param update:
        :param context:
        :return:
        """
        chat_id = update.callback_query.from_user.id
        first_name = update.callback_query.from_user.first_name
        message = Utils.get_start_message(opening="Ben ritornato/a", name=first_name)

        buttons = Utils.get_start_buttons()
        reply_markup = InlineKeyboardMarkup(buttons)

        context.bot.send_message(chat_id=chat_id,
                                 text=message,
                                 parse_mode=telegram.ParseMode.MARKDOWN_V2,
                                 reply_markup=reply_markup)

    @staticmethod
    def _course_button_handler(context: CallbackContext, text: str, chat_id: int) -> None:
        """

        :param context:
        :param text:
        :param chat_id:
        :return:
        """
        course_name = text.split('_')[0]
        Handlers.selected_course = course_name
        buttons = Utils.get_year_buttons(course_name)
        reply_markup = InlineKeyboardMarkup(buttons)
        message = f"Hai Scelto:\n{course_name}"
        context.bot.send_message(chat_id=chat_id,
                                 text=message,
                                 reply_markup=reply_markup)

    @staticmethod
    def _year_button_handler(context: CallbackContext, text: str, chat_id: int) -> None:
        """

        :param context:
        :param text:
        :param chat_id:
        :return:
        """
        year_name = text.split('__')[0]
        Handlers.selected_year = year_name
        buttons = Utils.get_subject_buttons(Handlers.selected_course, year_name)
        reply_markup = InlineKeyboardMarkup(buttons)
        message = f"Hai Scelto:\n{year_name.replace('_', ' ')}📚📚📚"
        context.bot.send_message(chat_id=chat_id,
                                 text=message,
                                 reply_markup=reply_markup,
                                 parse_mode=telegram.ParseMode.MARKDOWN_V2)

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
            Handlers._home_button_handler(update, context)
        else:
            if '_course' in text:
                Handlers._course_button_handler(context, text, chat_id)
            elif '__year' in text:
                Handlers._year_button_handler(context, text, chat_id)
        # TODO: back handler
