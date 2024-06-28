import os
import logging
import telegram
from dotenv import load_dotenv
import asyncio
from app.settings import TELEGRAM_BOT_TOKEN, YOUR_PERSONAL_CHAT_ID

load_dotenv()

logging.basicConfig(level=logging.DEBUG)


async def send_telegram_message(token, chat_id, message, parse_mode="Markdown"):
    try:
        bot = telegram.Bot(token=token)
        await bot.send_message(chat_id=chat_id, text=message, parse_mode=parse_mode)
        logging.info(f'Сообщение "{message}" отправлено в чат {chat_id}')
    except Exception as e:
        logging.error(f'Ошибка отправки сообщения в чат {chat_id}: {e}')