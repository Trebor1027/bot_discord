#IMAGENES DE SALUDO USANDO LA PALABRA "HOLA"
import discord as DC

imagenes = {
    "hola bayonetta": "https://i.pinimg.com/736x/5d/26/0f/5d260f0264dbfb254f1398c79ca5f2b1.jpg",
}

async def hola_imagen(message):
    if message.author.bot:
        return

    texto = message.content.lower().strip()
    if texto in imagenes:
        embed = DC.Embed()
        embed.set_image(url=imagenes[texto])
        await message.channel.send(embed=embed)
