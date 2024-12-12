import discord
from discord.ext import commands
from AntiScam import AntiScam

whitelist = [] # Here you can add the IDs of the users allowed to bypass the AntiScam system.
logs_channel = None # Here you can add the ID of the channel where the logs will be sent.

bot = commands.Bot(command_prefix='>')
bot.remove_command('help') # Remove this line if you want to use the help command.

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Moderar el Discord"))
    print("Iniciando... Keytan Link Blocker, estamos listos para bloquear.")

@bot.listen()
async def on_message(message):
    await AntiScam(message, bot = bot, whitelist = whitelist, muted_role='Muted', verified_role='Miembro', logs_channel=925238825062629397) # Here you can change the names of the roles.

bot.run('')
