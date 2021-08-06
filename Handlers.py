from Utils import Utils
import telegram


class Handlers:
    @staticmethod
    def start_handler(update, context) -> None:
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
        context.bot.send_photo(chat_id, doc)
        context.bot.send_message(chat_id, message, parse_mode=telegram.ParseMode.MARKDOWN_V2)
