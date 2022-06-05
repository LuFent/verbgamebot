import os
from telegram import Update
#from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from telegram.ext import CommandHandler, ContextTypes, MessageHandler, filters
from dialog import detect_intent_texts
from dotenv import load_dotenv
import logging


load_dotenv()


admin_id = os.environ['ADMIN_ID']

logger = logging.getLogger(__file__)
class TelegramLogsHandler(logging.Handler):

    def __init__(self, tg_bot, chat_id):
        super().__init__()
        self.chat_id = chat_id
        self.tg_bot = tg_bot

    def emit(self, record):
        message = self.format(record)
        self.tg_bot.send_message(chat_id=admin_id, text=message)


0/0

async def answer(update, context):
    await update.message.reply_text(detect_intent_texts(session_id=update.message.from_user,
                                                        project_id=os.environ['DIALOG_FLOW_ID'],
                                                        message=update.message.text,
                                                        language_code='ru')[0])


def main():
    logging.basicConfig(level=logging.ERROR)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(TelegramLogsHandler(bot, user_id))

    try:
        0/0

        tg_api_key = os.environ['TG_API_KEY']

        application = Application.builder().token(tg_api_key).build()
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, answer))
        application.run_polling()
    except Exception:



if __name__ == '__main__':
    main()
