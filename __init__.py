import asyncio

from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram import Client,filters
from pyrogram.types import *
import logging
from pyrogram.errors import (
    ChatAdminRequired
)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

bot=Client(":memory:",api_id="21073139",api_hash="e90297a18f44c384564182eb1cd1a27",bot_token="5963775988:AAE2Y1fdIoxV5PT0pTH-n7phxGFSgkJMCVw")

@bot.on_message(filters.command(["start", "agora"]))
async def hello(bot, message):
    await message.reply("Hello, This is a magical bot Group Management + Music bot + Security bot + Group Members adder bot!\n\n Simply Promote my By Adminstration with maximun admin rights and type /approve")
