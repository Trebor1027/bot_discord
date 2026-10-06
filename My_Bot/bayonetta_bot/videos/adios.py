#IMAGENES DE DESPEDIDA USANDO LA PALABRA "ADIOS"
import discord as DC

imagenes = {
    "adios bayonetta": "https://i.pinimg.com/736x/a1/c6/13/a1c6137f3baace2572c2820683b2be67.jpg",
}

async def adios_imagen(message):
    if message.author.bot:
        return

    texto = message.content.lower().strip()
    if texto in imagenes:
        embed = DC.Embed()
        embed.set_image(url=imagenes[texto])
        await message.channel.send(embed=embed)