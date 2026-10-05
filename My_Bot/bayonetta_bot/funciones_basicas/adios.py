from discord.ext import commands

#COMANDO PARA DESPEDIRSE CON !ADIOS
@commands.command()
async def adios(ctx):
    await ctx.send("adios cariño, nos vemos luego!")