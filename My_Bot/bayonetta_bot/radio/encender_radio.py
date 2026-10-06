import discord as DC
from discord.ext import commands

async def enviar_con_gif(ctx, texto, imagen_url):
    embed = DC.Embed(description=texto)
    embed.set_image(url=imagen_url)
    await ctx.send(embed=embed)

#COMANDO PARA ENCENDER LA RADIO
@commands.command()
async def radio(ctx):
    if ctx.voice_client is None:
        await ctx.send("Usa !unirse primero.")
        return  
    if ctx.voice_client.is_playing():
        ctx.voice_client.stop()

    url = "https://streams.deltaradio.de/uptempo/mp3-192/streams.deltaradio.de/"
    opciones = {
        "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
        "options": "-vn",
    }

    def al_terminar(error):
        print("Fin de reproducción:", error if error else "sin errores")

    ctx.voice_client.play(DC.FFmpegPCMAudio(url, **opciones), after=al_terminar)
    await enviar_con_gif(ctx, "voy a prender la radio cariño...",
                            "https://media.tenor.com/Of00Up8-_NEAAAAM/bayonetta-bayonetta-2.gif")
