from discord.ext import commands

#COMANDO PARA LIMPIAR EL CHAT CON !LIMPIAR
@commands.command()
async def limpiar(ctx):

    if ctx.author.id != ctx.guild.owner_id:
        await ctx.send("lo siento cariño, solo el anfitrión puede utilizar este comando.")
        return  

    await ctx.channel.purge(limit=None)