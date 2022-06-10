import random
import os
import vk_api as vk
from vk_api.longpoll import VkLongPoll, VkEventType
from dialog import detect_intent_texts
from dotenv import load_dotenv
import logging
from tg_handler import TelegramLogsHandler


logger = logging.getLogger(__file__)


def answer(event, vk_api):
    reply, is_fallback = detect_intent_texts(session_id=event.user_id,
                                        project_id=os.environ['DIALOG_FLOW_ID'],
                                        message=event.text,
                                        language_code="ru")

    if not is_fallback:
        vk_api.messages.send(
            user_id=event.user_id,
            message=reply,
            random_id=random.randint(1, 1000)
        )


def main():
    load_dotenv()
    logger.setLevel(logging.INFO)
    logger.addHandler(TelegramLogsHandler(tg_api_key, admin_id))
    vk_session = vk.VkApi(token=os.environ['VK_API_KEY'])
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            answer(event, vk_api)


if __name__ == '__main__':
    main()