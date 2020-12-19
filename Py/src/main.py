import logging
from aiogram import Bot, Dispatcher, executer, types

api_token = 'TOKEN'

logging.basicConfig(Level = logging.INFO)

bot = Bot(token=api_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
	await message.reply("Hello, world!")

@dp.message_handler()
async def start(message: types.Message):
	await message.answer(message.text)

if __name__ == '__main__':
	executer.start.pulling(dp, skip_updates=True)