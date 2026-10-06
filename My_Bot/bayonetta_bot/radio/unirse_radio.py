import discord as DC
from discord.ext import commands

async def enviar_con_imagen(ctx, texto, imagen_url):
    embed = DC.Embed(description=texto)
    embed.set_image(url=imagen_url)
    await ctx.send(embed=embed)

@commands.command()
async def unirse(ctx):
    if ctx.author.voice is None:
        await ctx.send("Primero entra a un canal de voz cariño")
        return

    canal = ctx.author.voice.channel

    if ctx.voice_client:
        # Ya está conectado: lo movemos a tu canal
        await ctx.voice_client.move_to(canal)
    else:
        # No está conectado: se une
        await canal.connect()

    await enviar_con_imagen(
        ctx,
        "bayonetta ha llegado a ponerle ritmo a este canal",
        "https://i.pinimg.com/originals/dc/9e/77/dc9e77f4114bcdf95e42e3a16fe3ed10.gif"
    )

    

  

