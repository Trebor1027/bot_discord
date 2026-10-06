import asyncio
import discord as DC
from discord.ext import commands
#COMANDO PARA SALIR DE LA RADIO CON IMAGEN     
async def enviar_con_imagen(ctx, texto, imagen_url):
    embed = DC.Embed(description=texto)
    embed.set_image(url=imagen_url)

    await ctx.send(embed=embed)
    
@commands.command()
async def salir(ctx):
    if ctx.voice_client:
        await enviar_con_imagen(ctx, "adios cariño, nos vemos luego!",
                            "https://media.tenor.com/Bc33I0RjNB8AAAAM/bayonetta-bayonetta-2.gif")
        await asyncio.sleep(1)
        await ctx.voice_client.disconnect()
    else:
        await ctx.send("No estoy en ningún canal de voz cariño")