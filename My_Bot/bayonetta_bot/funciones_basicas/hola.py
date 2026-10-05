from discord.ext import commands

#COMANDO PARA SALUDAR CON !HOLA
@commands.command()
async def hola(ctx):
    await ctx.send("hola cariño, quieres poner algo en la radio?")