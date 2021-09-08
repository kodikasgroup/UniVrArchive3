import telegram
from telegram import InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from ButtonGenerator import ButtonGenerator
from HashHandler import HashHandler
from Utils import Utils


class StartButtonHandler:
    @staticmethod
    def course_button_handler(context: CallbackContext, text: str, chat_id: int) -> None:
        """

        :param context:
        :param text:
        :param chat_id:
        :return:
        """
        course_name = text.split('_')[0]
        StartButtonHandler.selected_course = course_name
        buttons = ButtonGenerator.get_year_buttons(course_name)
        reply_markup = InlineKeyboardMarkup(buttons)
        message = f"Hai Scelto:\n{course_name}"
        context.bot.send_message(chat_id=chat_id,
                                 text=message,
                                 reply_markup=reply_markup)

    @staticmethod
    def year_button_handler(update: Update, context: CallbackContext, text: str, chat_id: int) -> None:
        """

        :param context:
        :param text:
        :param chat_id:
        :return:
        """

        split_text = text.split('/')
        course_name = split_text[0]
        year_name = split_text[1].split('__')[0]
        buttons = ButtonGenerator.get_subject_buttons(course_name, year_name)
        reply_markup = InlineKeyboardMarkup(buttons)
        message = f"Hai Scelto:\n{year_name.replace('_', ' ')}📚📚📚"
        Utils.delete_last_message(update, context)
        context.bot.send_message(chat_id=chat_id,
                                 text=message,
                                 reply_markup=reply_markup,
                                 parse_mode=telegram.ParseMode.MARKDOWN_V2)

    @staticmethod
    def subject_button_handler(update: Update, context: CallbackContext, text: str, chat_id: int):
        """

        :param update:
        :param context:
        :param text:
        :param chat_id:
        :return:
        """

        split_text = text.split('/')
        course_name = split_text[0]
        year_name = split_text[1]
        subject_name = split_text[2].split('__')[0]

        buttons = ButtonGenerator.get_subdir_buttons(course_name, year_name, subject_name)
        reply_markup = InlineKeyboardMarkup(buttons)
        message = "⏰Scegli il Materiale⏰"

        Utils.delete_last_message(update, context)
        context.bot.send_message(chat_id=chat_id,
                                 text=message,
                                 reply_markup=reply_markup,
                                 parse_mode=telegram.ParseMode.MARKDOWN_V2)

    @staticmethod
    def subdir_button_handler(update: Update, context: CallbackContext, text: str, chat_id: int):
        """

        :param update:
        :param context:
        :param text: the callback data in the following
               format `course/year/subject/DirectoryName__subdir`
        :param chat_id:
        :return:
        """

        split_text = text.split('/')
        course_name = split_text[0]
        year_name = split_text[1]
        subject_name = split_text[2]
        subdir_name = split_text[3].split("__")[0]

        buttons = ButtonGenerator.get_file_buttons(course_name, year_name, subject_name, subdir_name)
        reply_markup = InlineKeyboardMarkup(buttons)
        message = "💥ECCO IL MATERIALE DELLA SEZIONE💥"

        Utils.delete_last_message(update, context)
        context.bot.send_message(chat_id=chat_id,
                                 text=message,
                                 reply_markup=reply_markup,
                                 parse_mode=telegram.ParseMode.MARKDOWN_V2)

    @staticmethod
    def file_button_handler(update: Update, context: CallbackContext, text: str, chat_id: int):
        """

        :param update:
        :param context:
        :param text: the hashed callback data in the following
               format `course/year/subject/subdir/FileName__file`
        :param chat_id:
        :return:
        """

        text = text.split("__")[0]
        text = HashHandler.get_corresponding_text(text)
        split_text = text.split('/')
        course_name = split_text[0]
        year_name = split_text[1]
        subject_name = split_text[2]
        subdir_name = split_text[3]
        file_name = split_text[4]

        path = "archive" + "/" + course_name + "/" + year_name + "/" + subject_name + "/" + subdir_name + '/' + file_name
        file = open(path, 'rb')

        # TODO send file from telegram chat
        context.bot.send_document(
            chat_id=chat_id,
            document=file
        )

    @staticmethod
    def back_button_handler(update: Update, context: CallbackContext, text: str):
        """

        :param update:
        :param context:
        :param text:
        :return:
        """
        split_text = text.split('/')
        course_name = split_text[0]
        back_type = text.split('_')[-1]
        chat_id = update.callback_query.from_user.id

        if back_type == 'subject':
            Utils.delete_last_message(update, context)
            StartButtonHandler.course_button_handler(context, course_name + '_course', chat_id)
        elif back_type == 'subdir':
            param_text = '/'.join(split_text[:-1])
            StartButtonHandler.year_button_handler(update, context, param_text, chat_id)
        elif back_type == 'file':
            param_text = '/'.join(split_text[:-1])
            StartButtonHandler.subject_button_handler(update, context, param_text, chat_id)

    @staticmethod
    def home_button_handler(update: Update, context: CallbackContext) -> None:
        """

        :param update:
        :param context:
        :return:
        """
        chat_id = update.callback_query.from_user.id
        first_name = update.callback_query.from_user.first_name
        message = Utils.get_start_message(opening="Ben ritornato/a", name=first_name)

        buttons = ButtonGenerator.get_start_buttons()
        reply_markup = InlineKeyboardMarkup(buttons)

        Utils.delete_last_message(update, context)

        context.bot.send_message(chat_id=chat_id,
                                 text=message,
                                 parse_mode=telegram.ParseMode.MARKDOWN_V2,
                                 reply_markup=reply_markup)
