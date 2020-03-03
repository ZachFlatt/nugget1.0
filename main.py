import discord
from discord.ext import commands
import datetime
import os
import Nugget
from random import randint
import asyncio
from gtts import gTTS
import voice


#INVITE LINK: https://discordapp.com/api/oauth2/authorize?client_id=579480333083213854&permissions=8&scope=bot


app = discord.Client()
client = commands.Bot(command_prefix = '!/')
owner_id = 352478596289396737
leigon_id = 318536007358349322

#console output
@app.event
async def on_ready():
    time = datetime.datetime.now()
    print("Online at {}".format(time))

    acts = app.guilds
    mem = 0

    print("\nServers:")
    for s in acts:
        print(str(s.name))
        
    if str(s.name) == "Discord Bot List":
        return

    for a in acts:
        mem += len(a.members)

    print("\nMembers:", mem)

    await app.change_presence(activity=discord.Game(name='with {} users'.format(mem)))

@app.event
async def on_message(msg):
    if msg.content.startswith("!/hello"):
        await msg.channel.send("Hi")
    elif msg.content.startswith("!/goodbye"):
        await msg.channel.send("farewell")
    if msg.content.startswith("!/prefix"):
        await msg.channel.send("`My Prefix Is:` !/")


    elif msg.content.lower().startswith("!/tts"):
			  await voice.tts(msg, discord, os)

    elif msg.content.lower().startswith("!/welcometts"):
                          await msg.channel.send(file=discord.File("Welcome.wav".format(msg.id)))

    elif msg.content.startswith("!/work"):
			  await msg.channel.send("You started working")
			  await Nugget.work(msg.author.id, os)
			  await msg.channel.send("You have completed your shift {} and earned 15 nuggets".format(msg.author.mention))

    elif msg.content.lower().startswith("!/nuggets"):
			  await Nugget.bal(msg)
        
    elif msg.content.startswith("!/developernotes"):
        await msg.channel.send("`Here are your notes:`\n1. Add YouTube url audio streaming for vc2.\n2. Add buy command")



    if msg.content.startswith("!/ping"):
      await msg.channel.send(":ping_pong: `PONG`")

      
    if msg.content.lower().startswith("!/meme"):
        num = randint(0, 31)
        try:
            await msg.channel.send(file = discord.File("MEMES/{}.jpg".format(num))) 
        except:
            await msg.channel.send(file = discord.File("MEMES/{}.png".format(num)))

    if msg.content.startswith("!/invite"):
      invite = discord.Embed(title="Invite NuggetBOT", description="invite link for Nugget")
      invite.add_field(name="Link", value="https://discordapp.com/api/oauth2/authorize?client_id=579480333083213854&permissions=2048&scope=bot", inline=False)

      await msg.channel.send(content=None, embed=invite)

    if msg.content.startswith("!/help"):
      help = discord.Embed(title="Help", description="All possible commands for Nugget. Be sure to use !/ prefix before each command")
      help.add_field(name="Ping", value="Simply replies with Pong.", inline=False)
      help.add_field(name="Prefix", value="shows the currently set prefix", inline=False)
      help.add_field(name="meme", value="Sends random memes into the specified channel :P", inline=False,)
      help.add_field(name="power", value="I think you know what I mean :p XD", inline=False)
      help.add_field(name="developernotes", value="Shows possible future features for Nugget.", inline=False)
      help.add_field(name="xim", value="Gives links to XimMusic social and music streaming pages.", inline=False)
      help.add_field(name="Work", value="Work for nuggets(a completely useless bot currency", inline=False)
      help.add_field(name="Nuggets", value="Check how many nuggets(bot currency) you have.", inline=False)
      help.add_field(name="rolldye", value="Simply roles a six sided dice", inline=False)
      help.add_field(name="doggo", value="Sends cute dog images", inline=False)
      help.add_field(name="cat", value="Sends cute cat images", inline=False)
      help.add_field(name="tts", value="sends a tts file containg the contents of your message", inline=False)
      help.add_field(name="announcements", value = "Use this command to see all nugget related announcements", inline=False)

      announcement = discord.Embed(title="Nugget2.0 Coming Soon!!", description="\u200b")
      announcement.add_field(name="Nugget2.0 will soon be ready and on top.gg / discordbotlist to be added you your servers. Featuring new commands such as music, user info, and gambling/slot machine commands. Be sure to keep an eye out :D", value="\u200b", inline=False)

      
      await msg.channel.send(content=None, embed=help)
      await msg.channel.send(content=None, embed=announcement)

      

    if msg.content.startswith("!/power"):
        num = randint(1, 1)
        await msg.channel.send("```I HAVE THE POWWWEERRRRRR!!!```")
        await msg.channel.send(file = discord.File("Pic/{}.gif".format(num)))

    if msg.content.startswith("!/xim"):
        Xim = discord.Embed(title="XimMusic", description="A few links to XimMusic social and music",)
        Xim.add_field(name="YouTube", value="https://www.youtube.com/channel/UCI5FLkXh7TRWqnZx6btIDjw?view_as=subscriber",)
        Xim.add_field(name="SoundCloud", value="https://soundcloud.com/xentoro-hd",)
        Xim.add_field(name="Twitter", value="https://twitter.com/MusicXim", inline=False)
        await msg.channel.send(content=None, embed=Xim)

    elif msg.content.lower().startswith("!/rolldye"):
        num = randint(1, 6)
        await msg.channel.send(file = discord.File("DICE/{}.png".format(num)))

    elif msg.content.lower().startswith("!/doggo"):
        num = randint(1, 27)
        await msg.channel.send("```Aww look at that lil pupper!```")
        await msg.channel.send(file = discord.File("DOGGO/{}.jpg".format(num)))

        
    if msg.content.lower().startswith("!/cat"):
        num = randint(1, 32)
        await msg.channel.send("look at that lil creature XD")
        await msg.channel.send(file = discord.File("CAT/{}.jpg".format(num)))
        
        

app.run("NTc5NDgwMzMzMDgzMjEzODU0.XVRfXQ.gMW8g33FJJxrr7f7bfgBksnY72U")


