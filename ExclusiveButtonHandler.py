from telegram import InlineKeyboardMarkup
from telegram.ext import CallbackContext

from ExclusiveButtonGenerator import ExclusiveButtonGenerator
from HashHandler import HashHandler


class ExclusiveButtonHandler:
    @staticmethod
    def course_button_handler(context: CallbackContext, text: str, chat_id: int) -> None:
        """

        :param context:
        :param text: callback data from the clicked button
        :param chat_id: the id of the chat where to send the message
        :return:
        """
        hashed_course_name = text.split('#')[0]
        course_name = HashHandler.get_corresponding_text(hashed_course_name).split('/')[1]
        buttons = ExclusiveButtonGenerator.get_year_buttons(course_name)
        reply_markup = InlineKeyboardMarkup(buttons)
        message = "Hai scelto:\n" + \
                  f"{course_name}"
        context.bot.send_message(chat_id=chat_id,
                                 text=message,
                                 reply_markup=reply_markup)

    @staticmethod
    def exclusive_button_handler(context: CallbackContext, chat_id: int) -> None:
        """
        handles when the user clicks on the EXCLUSIVE button,
        it should display the buttons for choosing the course of study
        :param context:
        :param chat_id: the id of the chat where to send the message
        :return:
        """
        buttons = ExclusiveButtonGenerator.get_course_buttons()
        reply_markup = InlineKeyboardMarkup(buttons)
        message = "Eccoci nel area ⭐️Exclusive⭐\n" + \
                  "Qui i file che trovi hanno un COSTO in crediti indicato al inizio del nome" + \
                  "questo credito verra scalato una volta che si richiede il suddetto file" + \
                  "\n\nSi prega di non condividere i file con gli altri per rispetto degli sviluppatori e per poter " \
                  "usufruire di file nuovi"
        context.bot.send_message(chat_id=chat_id,
                                 text=message,
                                 reply_markup=reply_markup)
