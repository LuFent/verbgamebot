import logging
from telegram import Bot


class TelegramLogsHandler(logging.Handler):

    def __init__(self, tg_api_key, admin_id):
        super().__init__()
        self.chat_id = admin_id
        self.tg_bot = Bot(token=tg_api_key)

    def emit(self, record):
        message = self.format(record)
        self.tg_bot.send_message(chat_id=self.chat_id, text=message)