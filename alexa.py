token = input('Enter your bot token here! No quotes!')
import discord
import asyncio
nowplay = "ɴᴏᴡ ᴘʟᴀʏɪɴɢ: "
linebreak = "\u000A"
status = " ───────────:white_circle:────── ◄◄⠀▐▐ ⠀►►⠀⠀ ⠀ 𝟸:𝟷𝟾 / 𝟹:𝟻𝟼 ⠀ ─○─ :loud_sound:⠀ ᴴᴰ :gear:️ ❐ ⊏⊐"
client = discord.Client()
@client.event
async def on_ready():
    print('Logged on as:')
    print(client.user.name)
@client.event
async def on_message(message):
    if message.content.startswith('Alexa play'):
        song = message.content[11:]
        finalcontent = nowplay + song + linebreak + status
        await client.send_message(message.channel, finalcontent)
    if message.content.startswith('Alexa, play'):
        songcomma = message.content[12:]
        finalcontentcomma = nowplay + songcomma + linebreak + status
        await client.send_message(message.channel, finalcontentcomma)
    if message.content.startswith('Alexa help'):
        await client.send_message(message.channel, "Summon me by saying \"Alexa, play [song]\" or \"Alexa play [song]\".")
    if message.content.startswith('Alexa, help'):
        await client.send_message(message.channel, "Summon me by saying \"Alexa, play [song]\" or \"Alexa play [song]\".")
client.run(token)
