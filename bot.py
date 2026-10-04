import asyncio
import os
import discord as DC
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = DC.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} ha iniciado sesión.")

@bot.command()
async def hola(ctx):
    await ctx.send("hola, cariño. ¿Qué tal si ponemos algo de música")
    
@bot.command()
async def unirse(ctx):
    if ctx.author.voice is None:
        await ctx.send("Primero entra a un canal de voz.")
        return
    await ctx.send("me he unido al canal de voz, cariño.")
    await ctx.author.voice.channel.connect()
    
import os
    
@bot.command()
async def radio(ctx):
    if ctx.voice_client is None:
        await ctx.send("Usa !unirse primero.")
        return
    if ctx.voice_client.is_playing():
        ctx.voice_client.stop()

    url = "https://ice1.somafm.com/groovesalad-128-mp3"
    opciones = {
        "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
        "options": "-vn",
    }

    def al_terminar(error):
        print("Fin de reproducción:", error if error else "sin errores")

    ctx.voice_client.play(DC.FFmpegPCMAudio(url, **opciones), after=al_terminar)
    await ctx.send("voy a prender la radio...")
    
@bot.command()
async def pausa(ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
        ctx.voice_client.pause()

@bot.command()
async def reanudar(ctx):
    if ctx.voice_client and ctx.voice_client.is_paused():
        ctx.voice_client.resume()

@bot.command()
async def salir(ctx):
    if ctx.voice_client:
        await ctx.send("Me voy del canal de voz, cariño.hasta luego.")
        await asyncio.sleep(1)
        await ctx.voice_client.disconnect()
    else:
        await ctx.send("No estoy en ningún canal de voz, cariño.")
    

        
@bot.command()
async def repetir(ctx, *, texto):
    await ctx.send(texto + " cariño")


bot.run(os.environ["DISCORD_TOKEN"])