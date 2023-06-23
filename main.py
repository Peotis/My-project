from settings import settings
import discord
from discord.ext import commands
# import * - adalah cara cepat untuk mengimpor semua file di perpustakaan
from bot_logic import *

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan memindahkan hak istimewa
bot = commands.Bot(command_prefix='$', intents=intents)


# Setelah bot siap, ia akan mencetak namanya!
@bot.event()
async def on_ready():
    print(f'We have logged in as {bot.user}')

# Saat bot menerima pesan, bot akan mengirimkan pesan di saluran yang sama!
@bot.command()
async def on_ready():
    async def hello(ctx):
        await ctx.send(f'Hi! I am a bot {bot.user}!')
        embed = discord.Embed(title="Halo", description="bot ini di buat oleh clay", color=0x00ff00)
        embed.set_author(name="Kodland test bot", icon_url="https://pbs.twimg.com/media/FtYXfHyXgAgKcdl?format=png&name=small")
        embed.add_field(name="$listcommand", value="gunakan $listcommand, untuk mengetahui fungis bot ini", inline=False)
        embed.set_footer(text="mengenalkan saya adalah bot yang dari sebuah project")
        await ctx.send(embed=embed)

@bot.command()
async def smile(ctx):
    embed = discord.Embed(title="emoji", description="bot ini di buat oleh clay", color=0x00ff00)
    embed.set_author(name="Kodland test bot", icon_url="https://pbs.twimg.com/media/FtYXfHyXgAgKcdl?format=png&name=small")
    embed.add_field(name=gen_emodji(), value="ini adalah emoji yang kamu dapatkan", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def coin(ctx):
    embed = discord.Embed(title="flip a coin", description="bot ini di buat oleh clay", color=0x00ff00)
    embed.set_author(name="Kodland test bot", icon_url="https://pbs.twimg.com/media/FtYXfHyXgAgKcdl?format=png&name=small")
    embed.add_field(name=flip_coin(), value="ini adalah koin yang kamu dapatkan", inline=False)
    await  ctx.send(embed=embed)
    
@bot.command()
async def password(ctx):
    embed = discord.Embed(title="random a passowrd", description="bot ini di buat oleh clay", color=0x00ff00)
    embed.set_author(name="Kodland test bot", icon_url="https://pbs.twimg.com/media/FtYXfHyXgAgKcdl?format=png&name=small")
    embed.add_field(name=gen_pass(10), value="ini adalah password random yang kamu dapatkan", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def listcommand(ctx):
    embed = discord.Embed(title="ini adalah seluruh list command bot discordnya", description="bot ini di buat oleh clay", color=0x00ff00)
    embed.set_author(name="Kodland test bot", icon_url="https://pbs.twimg.com/media/FtYXfHyXgAgKcdl?format=png&name=small")
    embed.add_field(name=commands(), value="ini adalah semua command list yang kamu dapatkan", inline=False)
    await ctx.channel.send(embed=embed)
    
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

 
bot.run(settings["TOKEN"])
