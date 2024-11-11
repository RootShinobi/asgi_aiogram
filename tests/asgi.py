from asgi_aiogram import ASGIAiogram
from asgi_aiogram.strategy import SingleStrategy
from mini_app import dp, bot


app = ASGIAiogram(
    dispatcher=dp,
    strategy=SingleStrategy(bot=bot, path="/webhook"),
)

