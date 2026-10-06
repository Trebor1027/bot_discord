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
    ruta = os.path.join(os.path.dirname(__file__), "videos", "bayonetta.txt")
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
from radio.salir_radio import salir
bot.add_command(unirse)
bot.add_command(salir)


# COMANDO PARA ENCENDER LA RADIO
from radio.encender_radio import radio
bot.add_command(radio)


# COMANDO PARA PAUSAR, REANUDAR Y SALIR DE LA RADIO
from radio.funciones_radio import pausa, reanudar
bot.add_command(pausa)
bot.add_command(reanudar)


#-----------------------VIDEOS----------------------

#COMANDO PARA ENVIAR VIDEOS DE SALUDO, DESPEDIDA Y MEMES
from videos.presentacion import hola_imagen
from videos.adios import adios_imagen
from videos.meme import meme_imagen

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    await hola_imagen(message)
    await adios_imagen(message)
    await meme_imagen(message)
    await bot.process_commands(message)
    

#----------------------LIMPIAR CHAT----------------------

#COMANDO PARA LIMPIAR EL CHAT CON !LIMPIAR
from funciones_basicas.limpiar import limpiar
bot.add_command(limpiar)


#COMANDO PARA MOSTAR LOS COMANDOS DEL BOT
from funciones_basicas.decir_comandos import comandos
bot.add_command(comandos)

#----------------------EJECUCION----------------------
bot.run(os.environ["DISCORD_TOKEN"])

