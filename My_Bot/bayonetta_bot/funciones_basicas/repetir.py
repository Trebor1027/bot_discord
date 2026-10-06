import discord as DC
from discord.ext import commands

#COMANDO PARA ENVIAR UN MENSAJE CON UNA IMAGEN
async def enviar_con_imagen(ctx, texto, imagen_url):
    embed = DC.Embed(description=texto)
    embed.set_image(url=imagen_url)

    await ctx.send(embed=embed)

#COMANDO PARA REPETIR UN TEXTO CON !REPETIR
@commands.command()
async def repetir(ctx, *, texto):
    await enviar_con_imagen(ctx, texto + " cariño", "https://i.pinimg.com/originals/c7/f0/36/c7f03625e5ddbba5edf5cc1de7bcdcc4.gif")


