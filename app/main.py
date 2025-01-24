import logging
from contextlib import asynccontextmanager

from app.bot.create_bot import bot, dp, stop_bot, start_bot
from app.bot.handlers.router import router as bot_router
from aiogram.filters import CommandStart
from app.config import settings
from app.game.router import router as game_router
from fastapi.staticfiles import StaticFiles
from aiogram.types import Update, Message
from fastapi import FastAPI, Request

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

dp.include_router(bot_router)


"""
@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("Starting bot setup...")
    dp.include_router(bot_router)
    await start_bot()
    webhook_url = settings.get_webhook_url()
    await bot.set_webhook(url=webhook_url,
                          allowed_updates=dp.resolve_used_update_types(),
                          drop_pending_updates=True)
    logging.info(f"Webhook set to {webhook_url}")
    yield
    logging.info("Shutting down bot...")
    await bot.delete_webhook()
    await stop_bot()
    logging.info("Webhook deleted")
"""

app = FastAPI()
# app = FastAPI(lifespan=lifespan)


app.mount('/static', StaticFiles(directory='app/static'), 'static')


@app.post("/webhook")
async def bot_webhook(update: dict):
    await dp.feed_raw_update(bot, update)
    await bot.session.close()


"""
@app.post("/webhook")
async def webhook(request: Request) -> None:
    logging.info("Received webhook request")
    update = Update.model_validate(await request.json(), context={"bot": bot})
    await dp.feed_update(bot, update)
    logging.info("Update processed")
"""

app.include_router(game_router)


@app.get("/test")
def main_web_handler():
    return str(webhook_url)
