import os
import discord
from discord.ext.commands import Bot

TOKEN = ''

BOT_PREFIXES = ('!')
mybot = Bot(command_prefix=BOT_PREFIXES)

@mybot.command(pass_context=True)
async def save_image(context,message):
        imglist = os.listdir("$$$save_image")

mybot.run(TOKEN)






