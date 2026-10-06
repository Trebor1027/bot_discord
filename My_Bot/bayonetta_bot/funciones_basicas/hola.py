import discord as DC
from discord.ext import commands

#COMANDO PARA ENVIAR UN MENSAJE CON UNA IMAGEN
async def enviar_con_imagen(ctx, texto, imagen_url):
    embed = DC.Embed(description=texto)
    embed.set_image(url=imagen_url)

    await ctx.send(embed=embed)
    
#COMANDO PARA SALUDAR CON !HOLA
@commands.command()
async def hola(ctx):
    await enviar_con_imagen(ctx, "hola cariño, quieres poner algo en la radio?",
                            "https://tse1.mm.bing.net/th/id/OIP.mpA0XfGCWVsmvDmqiDC-mgHaHY?r=0&rs=1&pid=ImgDetMain&o=7&rm=3")
    




