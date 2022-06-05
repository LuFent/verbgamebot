import os
from telegram import Update, Bot
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater
from dialog import detect_intent_texts
from dotenv import load_dotenv
import logging


load_dotenv()

logger = logging.getLogger(__file__)


class TelegramLogsHandler(logging.Handler):

    def __init__(self, tg_api_key, admin_id):
        super().__init__()
        self.chat_id = admin_id
        self.tg_bot = Bot(token=tg_api_key)

    def emit(self, record):
        message = self.format(record)
        self.tg_bot.send_message(chat_id=self.chat_id, text=message)


def answer(update, context):
    update.message.reply_text(detect_intent_texts(session_id=update.message.from_user,
                                                        project_id=os.environ['DIALOG_FLOW_ID'],
                                                        message=update.message.text,
                                                        language_code='ru')[0])


def main():

    admin_id = os.environ['ADMIN_ID']
    tg_api_key = os.environ['TG_API_KEY']

    logger.setLevel(logging.INFO)

    logger.addHandler(TelegramLogsHandler(tg_api_key, admin_id))

    try:
        updater = Updater(token=tg_api_key, use_context=True)
        dispatcher = updater.dispatcher

        echo_handler = MessageHandler(Filters.text & (~Filters.command), answer)
        dispatcher.add_handler(echo_handler)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(TelegramLogsHandler(tg_api_key, admin_id))
        updater.start_polling()
        updater.idle()

    except Exception:
        logger.exception('Бот Упал :(\nОшибка:')


if __name__ == '__main__':
    main()
