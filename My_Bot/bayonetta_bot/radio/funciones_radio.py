import asyncio
from discord.ext import commands
import discord as DC

#COMANDOS PARA PAUSAR, REANUDAR Y SALIR DE LA RADIO
@commands.command()
async def pausa(ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
        ctx.voice_client.pause()
        
        
@commands.command()
async def reanudar(ctx):
    if ctx.voice_client and ctx.voice_client.is_paused():
        ctx.voice_client.resume()
        
    