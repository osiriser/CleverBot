from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config_reader import config
from aiogram import types
from aiogram.dispatcher import filters
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text
import openai

bot = Bot(token=config.bot_token.get_secret_value())
openai.api_key = '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'
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет! Напиши мне сообщение и я отвечу на него!\nHi! Write me a message and I will reply to it!")


@dp.message_handler()
async def send(message: types.Message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.9,
        max_tokens=4000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    await message.answer(response['choices'][0]['text'])




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
