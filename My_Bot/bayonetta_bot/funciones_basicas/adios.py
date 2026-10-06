from discord.ext import commands
import discord as DC


#COMANDO PARA DESPEDIRSE CON !ADIOS
async def enviar_con_gif(ctx, texto, imagen_url):
    embed = DC.Embed(description=texto)
    embed.set_image(url=imagen_url)

    await ctx.send(embed=embed)
    
#COMANDO PARA DESPEDIRSE CON !ADIOS CON GIF
@commands.command()
async def adios(ctx):
    await enviar_con_gif(ctx, "adios cariño, nos vemos luego!",
                            "https://media.tenor.com/Bc33I0RjNB8AAAAM/bayonetta-bayonetta-2.gif")