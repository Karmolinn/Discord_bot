import discord
from discord.ext.commands import Bot

TOKEN = '(token)'
BOT_PREFIXES = ('!')
mybot = Bot(command_prefix=BOT_PREFIXES)

@mybot.command(aliases=['tere', 'tervist'], pass_context=True)
async def hello(context):
    response = ['tere maailm']

    channel = context.channel
    await channel.send(response + ", " + context.message.author.mention)

mybot.run(TOKEN)
    
