token = input('Enter your bot token here! No quotes!')
import discord
import asyncio
nowplay = "ɴᴏᴡ ᴘʟᴀʏɪɴɢ: "
status = " ────────────────:white_circle:────────────────── ◄◄⠀▐▐ ⠀►►\n───○ 🔊ᴴᴰ ⚙️ ❐ ⊏⊐"
client = discord.Client()
@client.event
async def on_ready():
    print('Logged on as:')
    print(client.user.name)
@client.event
async def on_message(message):
    if message.content.startswith('Alexa play'):
        song = message.content[11:]
        finalcontent = nowplay + song + status
        await client.send_message(message.channel, finalcontent)
    if message.content.startswith('Alexa, play'):
        songcomma = message.content[12:]
        finalcontentcomma = nowplay + songcomma + status
        await client.send_message(message.channel, finalcontentcomma)
    if message.content.startswith('Alexa help'):
        await client.send_message(message.channel, "Summon me by saying \"Alexa, play songname\" or \"Alexa play songname\".")
    if message.content.startswith('Alexa, help'):
        await client.send_message(message.channel, "Summon me by saying \"Alexa, play songname\" or \"Alexa play songname\".")
client.run(token)