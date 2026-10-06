#IMAGENES DE MEMES USANDO LA PALABRA "UN MEME BAYONETTA"
import discord as DC

imagenes = {
    "un meme bayonetta": "https://tse2.mm.bing.net/th/id/OIP.ZXxQ85gq6NeQhGJSJmjn4QHaGk?r=0&rs=1&pid=ImgDetMain&o=7&rm=3",
}

async def meme_imagen(message):
    if message.author.bot:
        return

    texto = message.content.lower().strip()
    if texto in imagenes:
        embed = DC.Embed()
        embed.set_image(url=imagenes[texto])
        await message.channel.send(embed=embed)