from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from dialog import detect_intent_texts


#async def start(update, context):
#    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


#async def answer(update, context):
#    await update.message.reply_text(detect_intent_texts(message.text))


async def answer(update, context):
    await update.message.reply_text(detect_intent_texts(session_id=update.message.from_user,
                                                        project_id="newagent-dhxx",
                                                        message=update.message.text,
                                                        language_code="ru"))



def main():
    application = Application.builder().token('5518463606:AAG0DTysezhhXavWr7MAyWd2QMz7sSbqPAQ').build()

 #   start_handler = CommandHandler('start', start)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, answer))
 #   application.add_handler(start_handler)
    application.run_polling()


if __name__ == "__main__":
    main()
