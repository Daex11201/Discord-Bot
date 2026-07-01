import os
import discord
from dotenv import load_dotenv
from bot_logic import gen_pass

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Hemos iniciado sesión como {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hola"):
        await message.channel.send(f"Hola, soy un bot {bot.user}! como te va mi maledor, mi compa, mi femboy favorito")

    elif message.content.startswith("$chao"):
        await message.channel.send("Chao con vro, me hablas despues")

    elif message.content.startswith("$pass"):
        await message.channel.send("Tu contraseña: " + gen_pass(10))

    elif message.content.startswith("$Me_embargaron_la_casa_que_hago"):
        await message.channel.send("Vende droga")

    elif message.content.startswith("$contaminacion"):
        await message.channel.send("El uso de combustibles fósiles y las emisiones industriales liberan contaminantes como el CO₂.Provoca millones de muertes prematuras anuales por afecciones respiratorias")

    elif message.content.startswith("$Por_que_tienes_3_niños_en_tu_sotano"):
        await message.channel.send("No es secuestro, es adopcion sorpresa")

    else:
        await message.channel.send()


client.run(TOKEN)