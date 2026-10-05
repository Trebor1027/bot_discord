from discord.ext import commands


#COMANDO PARA UNIRSE A UN CANAL DE VOZ
@commands.command()
async def unirse(ctx):
    if ctx.author.voice is None:
        await ctx.send("Primero entra a un canal de voz.")
        return
    await ctx.send("me he unido al canal de voz, cariño.")
    await ctx.author.voice.channel.connect()