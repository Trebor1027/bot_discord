#LIBRERIAS
import os
import discord as DC
from discord.ext import commands
from dotenv import load_dotenv


#CARGAR VARIABLES DE ENTORNO
load_dotenv()

#CONFIGURAR INTENTS DEL BOT
intents = DC.Intents.default()
intents.message_content = True

# CREAR EL BOT
bot = commands.Bot(command_prefix='!', intents=intents)

# EVENTO DE CUANDO EL BOT ESTÁ LISTO
@bot.event
async def on_ready():
    ruta = os.path.join(os.path.dirname(__file__), "imagenes", "bayonetta.txt")
    try:
        with open(ruta, encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("(no se encontró bayonetta.txt)")
    print(f"¡{bot.user.name} ha llegado, cariño! El espectáculo está a punto de comenzar.")


#-----------------------FUNCIONES BASICAS----------------------
# COMANDO PARA SALUDAR
from funciones_basicas.hola import hola
bot.add_command(hola)

# COMANDO PARA DESPEDIRSE
from funciones_basicas.adios import adios
bot.add_command(adios)

# COMANDO PARA REPETIR
from funciones_basicas.repetir import repetir
bot.add_command(repetir)


#-----------------------RADIO----------------------

# COMANDO PARA UNIRSE A LA RADIO
from radio.unirse_radio import unirse
bot.add_command(unirse)


# COMANDO PARA ENCENDER LA RADIO
from radio.encender_radio import radio
bot.add_command(radio)


# COMANDO PARA PAUSAR, REANUDAR Y SALIR DE LA RADIO
from radio.funciones_radio import pausa, reanudar, salir
bot.add_command(pausa)
bot.add_command(reanudar)
bot.add_command(salir)


#-----------------------IMAGENES----------------------

#COMANDO PARA ENVIAR IMAGENES DE SALUDO, DESPEDIDA Y MEMES
from imagenes.hola import hola_imagen
from imagenes.adios import adios_imagen
from imagenes.meme import meme_imagen

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    await hola_imagen(message)
    await adios_imagen(message)
    await meme_imagen(message)
    await bot.process_commands(message)



#----------------------EJECUCION----------------------
bot.run(os.environ["DISCORD_TOKEN"])

