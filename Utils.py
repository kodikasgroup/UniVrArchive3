import os

from telegram import InlineKeyboardButton


class Utils:
    @staticmethod
    def get_start_message(opening: str, name: str) -> str:
        """
        composes the welcome message to send to the user based on input parameters
        :param opening: the welcome phrase (Benvetuto/a and Bentornato/a)
        :param name: the first name of the user
        :return: the message compose from given parameters
        """
        message = f"📘📗📙📘📗📙📘📗📙📘📗📙\n" + \
                  "Ciao 🍎{}🍎\n" + \
                  "{} nel bot UniVrInfoArchive\_bot, qui potrai trovare molto materiale che ti potrà essere d'aiuto per prepararti ai tuoi esami\.\n\n" + \
                  "Commandi che potrebbero esserti utili:\n" + \
                  "/credits mostra i crediti disponibili\n" + \
                  "/feedback \*messaggio\* se vuoi segnalarci qualcosa o darci consigli *[ovviamente il testo del messaggio senza asterischi]*\n" + \
                  "/info se ti servono informazioni\n" + \
                  "/exclusive per capire cos'è la sezione exclusive\n\n" + \
                  "Vuoi inviarci materiale ? Bene, basta che lo mandi sotto forma di file direttamente al bot\." + \
                  "Ti chiediamo cortesemente se hai piu file di creare una cartella compressa e poi inviarla\. " + \
                  "Una volta revisionati i file riceverai crediti da poter usare eventualmente nel area exclusive\.\n\n" + \
                  "📕📕📕Buon Studio 📕📕📕"
        message = message.format(name, opening)
        return message

    @classmethod
    def get_start_buttons(cls) -> list:
        """
        checks all the directories inside the archive directory
        then for each one it generates a button
        :return:
        """
        path = "archive"
        buttons = []
        for d_name in os.listdir(path):
            if d_name == "EXCLUSIVE":
                # append eight pointed black star to the front and the back of the button text
                button_text = "✴" + d_name + "✴"
                buttons.append([InlineKeyboardButton(button_text, callback_data=d_name)])
            else:
                # append pencil to the front and the back of the button text
                button_text = "✏" + d_name + "✏"
                buttons.append([InlineKeyboardButton(button_text, callback_data=d_name)])
        return buttons
