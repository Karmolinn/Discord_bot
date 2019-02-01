<<<<<<< HEAD
import urllib
import requests
import os
import discord
from discord.ext.commands import Bot

IMAGEDIRECTORY = "C:/Users/kalinnu/Desktop/Piltide_kaust/"
TOKEN = ''

BOT_PREFIXES = ('!')
mybot = Bot(command_prefix=BOT_PREFIXES)


@mybot.command(pass_context=True)
async def save_image(context, url, filename):
        response = requests.get(url)
        if response.status_code == 200:
                with open(IMAGEDIRECTORY + "/" + filename + '.jpg' , 'wb') as f:
                        f.write(response.content)


@mybot.command(pass_context=True)
async def display_image(context, filename):
        filename = IMAGEDIRECTORY + filename + ".jpg"
        print(filename)
        with open(filename, 'rb') as fp:
            await context.channel.send(file=discord.File(filename))

mybot.run(TOKEN)
=======
import urllib
import requests
import os
import discord
from discord.ext.commands import Bot

IMAGEDIRECTORY= "C:/Users/kalinnu/Desktop/Piltide_kaust"
TOKEN = ''

BOT_PREFIXES = ('!')
mybot = Bot(command_prefix=BOT_PREFIXES)

@mybot.command(pass_context=True)
async def save_image(context,url,filename):

        response = requests.get(url)
        if response.status_code == 200:
                with open(IMAGEDIRECTORY + "/" + filename, 'wb') as f:
                        f.write(response.content)
@mybot.command(pass_context=True)
async def upload(context,filename):

                img = open(IMAGEDIRECTORY + '/' + filename, 'rb')
                bot.send_chat_action(message.chat.id, "upload")
                bot.send_photo(message.chat.id, img)
                img.close()

        
mybot.run(TOKEN)
>>>>>>> f76ceeaed0a4ffb0e497d0decbe2e03fba5911bf
