import os
import discord
from discord import app_commands
from discord.ext import commands
from myserver import server_on

bot = commands.Bot(command_prefix='p!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot ready")
    synced = await bot.tree.sync()
    print(f"(len{synced}) command(s)")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1239224281284481134)
    text = f"Hello World, {member.mention}!"

    emmbed = discord.Embed(title = 'Welcome to My World', description = text, color = 0x66ffff)

    await channel.send(text)
    await channel.send(embed = emmbed)
    await member.send(text)

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1249552387476295780)
    text = f"{member.name} has left the server!"
    await channel.send(text)

@bot.event
async def on_message(message):
    mes = message.content
    if 'หวัดดี' in mes:
        await message.channel.send("หวัดไม่ดีนะ")

    if '0821689151' in mes :
        await message.channel.send("ผมบอทเองครับ")

    elif 'บอท' == mes:
        await message.channel.send("abd")

    await bot.process_commands(message)

@bot.command()
async def play(ctx, url):
    Get the voice channel that the user is in
    voice_channel = ctx.author.voice.channel

    If the user is not in a voice channel, return an error message
    if not voice_channel:
        await ctx.send("You must be in a voice channel to use this command.")
        return

    Join the voice channel
    await voice_channel.connect()

    Play the song
    player = await voicechannel.createytdl_player(url)
    player.start()


@bot.command()
async def HELP(ctx):
    await ctx.send("""พิมพ์ 'p!' แล้วตามด้วยคำสั่ง \n help = ก็ดูข้อมูลนี้แหละเออ \n play =  ตามด้วยชื่อเพลงหรือลิงค์ เพื่อเปิดเพลง
                    """)
    
@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.tree.command(name="do_not_use_this", description='ฉันคือบอท เผื่อไม่รู้')
async def helppcommand(interaction):
    await interaction.response.send_message("""ฉันคือบอท เผื่อไม่รู้ \n พิมพ์ 'p!' แล้วตามด้วยคำสั่ง \n help = ก็ดูข้อมูลนี้แหละเออ \n play =  ตามด้วยชื่อเพลงหรือลิงค์ เพื่อเปิดเพลง \n
                                            """)

@bot.tree.command(name='name')
# @app_commands.describe(name = "What's your name?")
async def namecommand(interaction):
# async def namecommand(interaction, name : str):
    await interaction.response.send_message(f"หวัดดี {user_name}")

#embed
@bot.tree.command(name='help', description='คู่มือบอท')
async def helppcommand(interaction):
    emmbed = discord.Embed(title='ช่วยด้วย! - คู่มือบอท', 
                           description='คู่มือบอท',
                             color=0x66ffff,
                               timestamp= discord.utils.utcnow())


    emmbed.add_field(name='/hello1', value='Hello Command\n', inline=True)    
    emmbed.add_field(name='/hello2', value='Hello Command\n', inline=True)
    emmbed.add_field(name='/hello3', value='Hello Command', inline=False)

    emmbed.set_author(name='กดเพื่อวาป', url='https://www.instagram.com/gg_xpex/', icon_url='https://media1.tenor.com/m/5oQ9_1CpCuoAAAAd/spooky-month-spooky-season.gif')

    emmbed.set_thumbnail(url='https://media1.tenor.com/m/HwGJ_4uXGU4AAAAd/stare-cat-stare.gif')
    emmbed.set_image(url='https://media1.tenor.com/m/dd2Q9t5km5YAAAAd/computer-pc.gif')

    emmbed.set_footer(text='Footer', icon_url='https://media1.tenor.com/m/5oQ9_1CpCuoAAAAd/spooky-month-spooky-season.gif')

    await interaction.response.send_message(embed = emmbed)

server_on()
bot.run(os.getenv("TOKEN"))
