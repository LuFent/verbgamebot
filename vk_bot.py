import random
import os
import vk_api as vk
from vk_api.longpoll import VkLongPoll, VkEventType
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


def answer(event, vk_api):
    reply, status = detect_intent_texts(session_id=event.user_id,
                                        project_id=os.environ['DIALOG_FLOW_ID'],
                                        message=event.text,
                                        language_code="ru")

    if not status:
        vk_api.messages.send(
            user_id=event.user_id,
            message=reply,
            random_id=random.randint(1, 1000)
        )



if __name__ == '__main__':
    logger.setLevel(logging.INFO)
    logger.addHandler(TelegramLogsHandler(tg_api_key, admin_id))
    vk_session = vk.VkApi(token=os.environ['VK_API_KEY'])
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            answer(event, vk_api)