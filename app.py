from aiogram import Bot, Dispatcher, types
from asyncio import run
from aiogram.filters import CommandStart


token="7308500722:AAEOZYBHXYgJZPGSftsPaOLXSwsire5wdms"
bot = Bot(token=token)
dp=Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(f"Hello World")



async def main():
    await dp.start_polling(bot)

if __name__=='__main__':
    run(main())