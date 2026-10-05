import asyncio
from discord.ext import commands


#COMANDOS PARA PAUSAR, REANUDAR Y SALIR DE LA RADIO
@commands.command()
async def pausa(ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
        ctx.voice_client.pause()
        
        
@commands.command()
async def reanudar(ctx):
    if ctx.voice_client and ctx.voice_client.is_paused():
        ctx.voice_client.resume()
        
        
@commands.command()
async def salir(ctx):
    if ctx.voice_client:
        await ctx.send("Me voy del canal de voz, cariño.hasta luego.")
        await asyncio.sleep(1)
        await ctx.voice_client.disconnect()
    else:
        await ctx.send("No estoy en ningún canal de voz, cariño.")