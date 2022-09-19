from discord.ext import commands
import discord
import random

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is online and ready to use")

@bot.command()
async def towers(ctx):
        tower1,tower2,tower3,tower4,tower5,tower6,tower7,tower8,tower9,tower10,tower11,tower12,tower13,tower14,tower15,tower16,tower17,tower18,tower19,tower20,tower21,tower22,tower23,tower24 = "<:ocross:1020955346606501898>","<:ocross:1020955346606501898>","<:ocross:1020955346606501898>","<:ocross:1020955346606501898>","<:ocross:1020955346606501898>","<:ocross:1020955346606501898>","<:ocross:1020955346606501898>","<:ocross:1020955346606501898>","<:ocross:1020955346606501898>","<:ocross:1020955346606501898>","<:ocross:1020955346606501898>","<:ocross:1020955346606501898>","<:ocross:1020955346606501898>","<:ocross:1020955346606501898>","<:ocross:1020955346606501898>","<:ocross:1020955346606501898>","<:ocross:1020955346606501898>","<:ocross:1020955346606501898>","<:ocross:1020955346606501898>","<:ocross:1020955346606501898>","<:ocross:1020955346606501898>","<:ocross:1020955346606501898>","<:ocross:1020955346606501898>","<:ocross:1020955346606501898>"
        a = random.randint(1, 3)
        b = random.randint(1, 3)
        c = random.randint(1, 3)
        d = random.randint(1, 3)
        e = random.randint(1, 3)
        f = random.randint(1, 3)
        g = random.randint(1, 3)
        h = random.randint(1, 3)

        if a == 1:
            tower1 = "<:silver:1020955285768118363>"
        elif a == 2:
            towe2 = "<:silver:1020955285768118363>"
        elif a ==3:
            tower3 = "<:silver:1020955285768118363>"
        if b == 1:
            tower4 = "<:silver:1020955285768118363>"
        elif b == 2:
            tower5 = "<:silver:1020955285768118363>"
        elif b ==3:  
            tower6 = "<:silver:1020955285768118363>"
        if c == 1:
            tower7 = "<:silver:1020955285768118363>"
        elif c == 2:
            tower8 = "<:silver:1020955285768118363>"
        elif c ==3:
            tower9 = "<:silver:1020955285768118363>"
        if d == 1:
            tower10 = "<:silver:1020955285768118363>"
        elif d == 2:
            tower11 = "<:silver:1020955285768118363>"
        elif d ==3:
            tower12 = "<:silver:1020955285768118363>"
        if e == 1:
            tower13 = "<:silver:1020955285768118363>"
        elif e == 2:
            tower14 = "<:silver:1020955285768118363>"
        elif e ==3:
            tower15 = "<:silver:1020955285768118363>"
        if f == 1:
            tower16 = "<:silver:1020955285768118363>"
        elif f == 2:
            tower17 = "<:silver:1020955285768118363>"
        elif f ==3:
            tower18 = "<:silver:1020955285768118363>"
        if g == 1:
            tower19 = "<:silver:1020955285768118363>"
        elif g == 2:
            tower20 = "<:silver:1020955285768118363>"
        elif g ==3:
            tower21 = "<:silver:1020955285768118363>"
        if h == 1:
            tower22 = "<:silver:1020955285768118363>"
        elif h == 2:
            tower23 = "<:silver:1020955285768118363>"
        elif h ==3:
            tower24 = "<:silver:1020955285768118363>"

        row1 = tower1 + tower2 + tower3
        row2 = tower4 + tower5 + tower6
        row3 = tower7 + tower8 + tower9
        row4 = tower10 + tower11 + tower12
        row5 = tower13 + tower14 + tower15
        row6 = tower16 + tower17 + tower18
        row7 = tower19 + tower20 + tower21
        row8 = tower22 + tower23 + tower24
        #await ctx.send(row1 + "\n" + row2 + "\n" + row3 + "\n" +row4 + "\n" +row5 + "\n" +row6 + "\n" +row7 + "\n" +row8)
        
        
        list = [0x23272A, 0x23272A, 0x23272A, 0x23272A]
        color = random.choice(list)
        em = discord.Embed(color=color)
        info = str(random.randint(45, 95))

        em.set_footer(text="")
        em.add_field(name="Epileps Predictor", value=row1 + "\n" + row2 + "\n" + row3 + "\n" +row4 + "\n" +row5 + "\n" +row6 + "\n" +row7 + "\n" +row8 + "\n" + "" + "\n"  + "")   
        await ctx.send(embed=em)


bot.run('ODI5NDYwMjUzODgzNjI5Njcw.G8suNd.MIPzl7CKbeRuYulS3KTQ5yKW6wNPd8MPHYRuQU')