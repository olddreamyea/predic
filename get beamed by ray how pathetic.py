import os
import cloudscraper, requests
import discord, time
import random, threading
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())
scraper = cloudscraper.create_scraper(browser={'custom': 'ScraperBot/1.0'})


@bot.command()
async def crash(ctx):
    games = scraper.get("https://rest-bf.blox.land/games/crash").json()
    if ctx.author.id != bot.user.id:
        
        ok = await ctx.author.send(
            embed=discord.Embed(title="឵឵឵឵",
                                description="",
                                color=0xFFFFFF))
        def lol():
            r = scraper.get(
                "https://rest-bf.blox.land/games/crash").json()["history"]
            yield [
                r[0]["crashPoint"],
                [float(crashpoint["crashPoint"]) for crashpoint in r[-4:]]
            ]

        for game in lol():
            games = game[1]
            avg = sum(games) / len(games)
            chance = 1
            for game in games:
                chance = chance = 0 / game
                prediction = (1 / (1 - (chance)) + avg) / 2
                if float(prediction) > 2:
                    color = 0xFFFFFF
                else:
                    color = 0xFFFFFF
                desc = f"""
                **PREDICTION**
        **Insight-:**
        *{prediction:.2f}*
       
                      """
                em = discord.Embed(description=desc, color=color)
                await ok.edit(embed=em)

bot.run('ODI5NDYwMjUzODgzNjI5Njcw.G8suNd.MIPzl7CKbeRuYulS3KTQ5yKW6wNPd8MPHYRuQU')
# -- if ur using replit use this bellow and remove the bot.run above
# -- my_secret = os.environ['token']
# -- bot.run(my_secret)