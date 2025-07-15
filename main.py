# hodlerkurs_bot/main.py

import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import BotCommand

from handlers.trending import router as trending_router
from handlers.converter import router as converter_router
from handlers.portfolio import router as portfolio_router
from handlers.analysis import router as analysis_router
from handlers.forecast import router as forecast_router
from handlers.alerts import router as alerts_router
from handlers.prices import router as prices_router
from handlers.lang import router as lang_router

BOT_TOKEN = ""8108437127:AAEMgCtFigsuc-1WKX6V16pPyQdefcD6mCQ""  # BotFather'dan olingan token

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

dp.include_router(lang_router)
dp.include_router(prices_router)
dp.include_router(converter_router)
dp.include_router(portfolio_router)
dp.include_router(analysis_router)
dp.include_router(forecast_router)
dp.include_router(alerts_router)
dp.include_router(trending_router)

async def set_commands():
    commands = [
        BotCommand(command="start", description="Botni boshlash"),
        BotCommand(command="trend", description="Trenddagi coinlar (CoinGecko)"),
        BotCommand(command="kurslar", description="Top 10 coin kurslari"),
        BotCommand(command="convert", description="Kripto konvertor"),
        BotCommand(command="portfel", description="Shaxsiy portfel"),
        BotCommand(command="tahlil", description="Coin tahlili"),
        BotCommand(command="prognoz", description="Tahlil va prognozlar"),
        BotCommand(command="alert", description="Narx ogohlantirish")
    ]
    await bot.set_my_commands(commands)

async def main():
    await set_commands()
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
