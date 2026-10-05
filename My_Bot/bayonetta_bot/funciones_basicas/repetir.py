import discord
from discord.ext import commands

#COMANDO PARA REPETIR UN TEXTO CON !REPETIR
@commands.command()
async def repetir(ctx, *, texto):
    await ctx.send(texto + " cariño")
