import os
import time
import logging

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('TOKEN_TG')
MSG = "Программировал ли ты сегодня, {}?"

# Экземпляр класса бота
bot = Bot(token=TOKEN)

# Экземпляр класс диспетчера
dp = Dispatcher(bot=bot)


# Декоратор для входящих сообщений (команд)
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    """ Функция для обработки входящего сообщения (команды) """
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')

    await message.reply(f"Привет, {user_full_name}!")

    for i in range(7):
        """ Цикл для отправки MSG один раз в сутки в течение семи дней"""
        time.sleep(60*60*24)

        await bot.send_message(user_id, MSG.format(user_name))


if __name__ == '__main__':
    executor.start_polling(dp)
