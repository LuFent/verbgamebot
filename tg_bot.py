import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from dialog import detect_intent_texts
from dotenv import load_dotenv


load_dotenv()


async def answer(update, context):
    await update.message.reply_text(detect_intent_texts(session_id=update.message.from_user,
                                                        project_id=os.environ['DIALOG_FLOW_ID'],
                                                        message=update.message.text,
                                                        language_code='ru')[0])


def main():

    tg_api_key = os.environ['TG_API_KEY']

    application = Application.builder().token(tg_api_key).build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, answer))
    application.run_polling()


if __name__ == '__main__':
    main()
