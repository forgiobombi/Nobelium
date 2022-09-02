import discord
from discord.ext import commands
import logging
import os

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s » %(message)s')

intents = discord.Intents.all()


class MyBot(commands.Bot):
    async def setup_hook(self):
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await bot.load_extension(f"cogs.{filename[:-3]}")
                logging.info(f"{filename} Loaded!")

            else:
                logging.error(f"Impossible Loading {filename}.")
        
        print('Nobelium Bot setup completed')

bot = MyBot(command_prefix=';', intents=intents, activity=discord.Activity(type=discord.ActivityType.playing, name='Nobelium Bot'))


@bot.event
async def on_ready():
    print("Nobelium Bot Running")

@bot.event
async def on_connect():
    print("Nobelium Connected to Discord")



@bot.command(
    name='unload',
    description='Unloads cog from the bot.',
    usage='£unload (Cog)',
    brief='Unload cog',
    aliases=["ul"]
    )
@commands.has_role(859467091639009350)
async def unload(ctx, extension = None):
    if extension != None:
        await bot.unload_extension(f'cogs.{extension}')

        embed = discord.Embed(description=f":no_entry: Unloaded `cogs.{extension}`", color=discord.Color.dark_green())
        await ctx.reply(embed=embed)
    
    else:
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await bot.unload_extension(f'cogs.{filename[:-3]}')
        
        embed = discord.Embed(description=f":ballot_box_with_check: Unloaded all cogs", color=discord.Color.dark_green())
        await ctx.reply(embed=embed)



@bot.command(
    name='reload',
    description='Reload cog from the bot.',
    usage='£reload (Cog)',
    brief='Reload cog',
    aliases=["rl"]
    )
#@commands.has_role(859467091639009350)
async def reload(ctx, extension = None):
    if extension != None:
        await bot.reload_extension(f'cogs.{extension}')
        
        embed = discord.Embed(description=f"🔄 Reloaded `cogs.{extension}`", color=discord.Color.dark_green())
        await ctx.reply(embed=embed)
    
    else:
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await bot.reload_extension(f'cogs.{filename[:-3]}')

        embed = discord.Embed(description=f"🔄 Reloaded all cogs", color=discord.Color.dark_green())
        await ctx.reply(embed=embed)



@bot.command(
    name='load',
    description='Loads cog from the bot.',
    usage='£load (Cog)',
    brief='Load cog',
    aliases=["ld"]
    )
@commands.has_role(859467091639009350)
async def load(ctx, extension = None):
    if extension != None:
        await bot.load_extension(f'cogs.{extension}')

        embed = discord.Embed(description=f":ballot_box_with_check: Loaded `cogs.{extension}`", color=discord.Color.dark_green())
        await ctx.reply(embed=embed)
    
    else:
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await bot.load_extension(f'cogs.{filename[:-3]}')
        
        embed = discord.Embed(description=f":ballot_box_with_check: Loaded all cogs", color=discord.Color.dark_green())
        await ctx.reply(embed=embed)
    


@unload.error
@load.error
#@reload.error
async def handler(ctx, error):
    if isinstance(error, commands.MissingRole):
        embed = discord.Embed(
            description=":x: You don't have the permission to use this command.", color=discord.Color.red())
        await ctx.reply(embed=embed)
    elif isinstance(error, commands.ExtensionAlreadyLoaded):
        embed = discord.Embed(
            description=":x: Extension already loaded.", color=discord.Color.red())
        await ctx.reply(embed=embed)
    else:
        print(error)


bot.run(os.getenv('NOBELIUM_TOK'))