""" $hola
$chao
$passw
$dado
$Me_embargaron_la_casa_que_hago
$mem
$contaminacion
$Por_que_tienes_3_niños_en_tu_sotano
$gases_industriales"""

import random
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from bot_logic import gen_pass

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"Hemos iniciado sesión como {bot.user}")

@bot.command()
async def hola(ctx):
    await ctx.send(f"Hola, soy un bot {bot.user}! como te va mi maledor, mi compa, mi femboy favorito")

@bot.command()
async def chao(ctx):
    await ctx.send("Chao con vro, me hablas despues")

@bot.command()
async def Me_embargaron_la_casa_que_hago(ctx):
    await ctx.send("Vende droga")

@bot.command()
async def passw(ctx):
    await ctx.send("Tu contraseña: " + gen_pass(10))

@bot.command()
async def dado(ctx):
    import random
    await ctx.send(f"En el dado salió: {random.randint(1, 6)} ojala te hubiera salido en el casino y no conmigo XDD")

@bot.command()
async def Por_que_tienes_3_niños_en_tu_sotano(ctx):
    await ctx.send("No es secuestro, es adopcion sorpresa")

@bot.command()
async def contaminacion(ctx):
    await ctx.send("El uso de combustibles fósiles y las emisiones industriales liberan contaminantes como el CO₂.Provoca millones de muertes prematuras anuales por afecciones respiratorias")

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir("Memes"))

    with open(f"Memes/{img_name}", "rb") as f:
        picture = discord.File(f)

    await ctx.send(file=picture)

@bot.command()
async def gases_industriales(ctx):
    img_name = random.choice(os.listdir("Polucion"))

    with open(f"Polucion/{img_name}", "rb") as f:
        picture = discord.File(f)

    await ctx.send(file=picture)


bot.run(TOKEN)
