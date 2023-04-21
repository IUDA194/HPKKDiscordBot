import discord
from discord.ext import commands
import asyncio
from discord import utils
from config import settings

intents = discord.Intents.all() # Подключаем "Разрешения"
intents.message_content = True
bot = commands.Bot(command_prefix = settings['prefix'], intents=intents) # Инициализируем клас бота

@bot.event
async def on_message(ctx : discord.message.Message): # Хендлер на любое сообщение
    if ctx.content.startswith(f'{settings["prefix"]}del'): # Проверка является ли сообщения командой
        for i in ctx.guild.members: # Получаем список всех пользователей и проходимся по нему
            for n in i.roles: # Проходимся по всем ролям конкретного пользователя
                if n.name == settings['role_name']: # Проверка есть ли нужная нам роль
                    try:
                        await ctx.channel.send(f"{i.name} | was kiked")
                        print(f"{i.name} | was kiked")
                        await i.kick() # Кикаем человека
                    except:
                        pass


# Сообщение при подключение бота к серверу
@bot.event
async def on_guild_join(guild : discord.guild.Guild):
    ctx =  guild.get_channel(guild.channels[0].id)
    await ctx.text_channels[0].send("Hi all, I'm ready to work")


bot.run(settings['token']) # Обращаемся к словарю settings с ключом token, для получения токена
