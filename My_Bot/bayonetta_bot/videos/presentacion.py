from pathlib import Path
import discord as DC

CARPETA = Path(__file__).parent  # carpeta donde está hola.py

# lo que escribe el usuario -> (frase del bot, archivo de vídeo)
respuestas = {
    "quien es bayonetta": (
        "Soy Bayonetta cariño una bruja cazadora de ángeles y la mejor compañía que le podrías pedir a esta radio?",
        CARPETA / "bayonetta_discord.mp4",
    ),
}

async def hola_imagen(message):
    if message.author.bot:
        return

    texto = message.content.lower().strip()
    if texto in respuestas:
        frase, ruta = respuestas[texto]

        if not ruta.exists():
            print(f"No encuentro el archivo: {ruta}")
            return

        await message.channel.send(content=frase, file=DC.File(ruta))