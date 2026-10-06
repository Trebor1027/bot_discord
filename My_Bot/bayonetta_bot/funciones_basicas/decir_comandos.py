from discord.ext import commands
import discord as DC

@commands.command()
async def comandos(ctx):
    texto = (
        "Mmm, ¿quieres saber qué puedo hacer por ti, cariño? Ponte cómodo...\n\n"
        "**Para charlar conmigo**\n"
        "`!hola` - un saludito, que no muerdo\n"
        "`!adios` - me despido de ti, aunque me vas a echar de menos\n"
        "`!comandos` - te enseño todo lo que sé hacer, y te sorprenderás\n"
        "`!repetir` - dime algo bonito y yo te lo repito\n"
        "`!limpiar` - hago desaparecer mensajes sin dejar rastro (solo admins)\n\n"
        "**Para la radio**\n"
        "`!unirse` - entro a tu canal de voz, cariño\n"
        "`!salir` - me marcho del canal, con estilo\n"
        "`!radio` - enciendo la radio y le pongo ritmo a la noche\n"
        "`!pausa` - pauso la música... para que me prestes atención\n"
        "`!reanudar` - vuelvo a encender la radio, ¿por dónde íbamos?"
        
        
        
    )
    await ctx.send(texto)