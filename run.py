from discord.ext import commands
import discord
import re, requests
from colorama import Fore, init
init()
 
token = input("Enter your token:") # just replace it here with your token if you don't want to enter it each time
while 1:
	try:
		bot = commands.Bot(command_prefix=".", self_bot=True)
 
		@bot.event
		async def on_ready():
			print("[+] Bot is ready")
 
		@bot.event
		async def on_message(ctx):
			if 'discord.gift' in ctx.content:
				code = re.search("discord.gift/(.*)", ctx.content).group(1)
				if len(code) != 16:
					print("[=] Auto-detected a fake code : "+code)
				else:
					print(Fore.LIGHTGREEN_EX+"[-] Snipped code : "+code+" From "+ctx.author.name+"#"+ctx.author.discriminator)
					r = requests
					result = r.post('https://discordapp.com/api/v6/entitlements/gift-codes/'+code+'/redeem', json={"channel_id":str(ctx.channel.id)}, headers={'authorization':token}).text
					if 'This gift has been redeemed already.' in result:
						print(Fore.YELLOW+"[-] Code has been already redeemd : "+code+Fore.RESET)
					elif 'nitro' in result:
						print(Fore.GREEN+"[+] Code applied : "+code+Fore.RESET)
					elif 'Unknown Gift Code' in result:
						print(Fore.RED+"[-] Invalid Code : "+code+Fore.RESET)
# made by yz cuwl dude :sunglasses:
 
		bot.run(token, bot=False)
	except KeyError:
		pass