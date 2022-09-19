from discord.ext import commands
import discord
import random

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@bot.command()
async def mines(ctx):
        mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = '<:booom:1020955694075224124>', '<:booom:1020955694075224124>', '<:booom:1020955694075224124>', '<:booom:1020955694075224124>', '<:booom:1020955694075224124>', '<:booom:1020955694075224124>', '<:booom:1020955694075224124>', '<:booom:1020955694075224124>', '<:booom:1020955694075224124>', '<:booom:1020955694075224124>', '<:booom:1020955694075224124>', '<:booom:1020955694075224124>', '<:booom:1020955694075224124>', '<:booom:1020955694075224124>', '<:booom:1020955694075224124>', '<:booom:1020955694075224124>', '<:booom:1020955694075224124>', '<:booom:1020955694075224124>', '<:booom:1020955694075224124>', '<:booom:1020955694075224124>', '<:booom:1020955694075224124>', '<:booom:1020955694075224124>', '<:booom:1020955694075224124>', '<:booom:1020955694075224124>', '<:booom:1020955694075224124>'
        a = random.randint(1, 8)
        b = random.randint(9, 13)
        c = random.randint(14, 17)
        d = random.randint(18  , 25)
        if a == 1:
            mine1 = "<:bobuxx:1020955662362091560>"
        elif a == 2:
            mine2 = "<:bobuxx:1020955662362091560>"
        elif a == 3:
            mine3 = "<:bobuxx:1020955662362091560>"
        elif a == 4:
            mine4 = "<:bobuxx:1020955662362091560>"
        elif a == 5:
            mine5 = "<:bobuxx:1020955662362091560>"
        elif a == 6:
            mine6 = "<:bobuxx:1020955662362091560>"
        elif a == 7:
            mine7 = "<:bobuxx:1020955662362091560>"
        elif a == 8:
            mine8 = "<:bobuxx:1020955662362091560>"
        if b == 9:
            mine9 = "<:bobuxx:1020955662362091560>"
        elif b == 10:
            mine10 = "<:bobuxx:1020955662362091560>"
        elif b == 11:
            mine11 = "<:bobuxx:1020955662362091560>"
        elif b == 12:
            mine12 = "<:bobuxx:1020955662362091560>"
        elif b == 13:
            mine13 = "<:bobuxx:1020955662362091560>"
        if c == 14:
            mine14 = "<:bobuxx:1020955662362091560>"
        elif c == 15:
            mine15 = "<:bobuxx:1020955662362091560>"
        elif c == 16:
            mine16 = "<:bobuxx:1020955662362091560>"
        elif c == 17:
            mine17 = "<:bobuxx:1020955662362091560>"
        if d == 18:
            mine18 = "<:bobuxx:1020955662362091560>"
        elif d == 19:
            mine19 = "<:bobuxx:1020955662362091560>"
        elif d == 20:
            mine20 = "<:bobuxx:1020955662362091560>"
        elif d == 21:
            mine21 = "<:bobuxx:1020955662362091560>"
        elif d == 22:
            mine22 = "<:bobuxx:1020955662362091560>"
        elif d == 23:
            mine23 = "<:bobuxx:1020955662362091560>"
        elif d == 24:
            mine24 = "<:bobuxx:1020955662362091560>"
        elif d == 25:
            mine25 = "<:bobuxx:1020955662362091560>"
        row1 = mine1 + mine2 + mine3 + mine4 + mine5

        row2 = mine6 + mine7 + mine8 + mine9 + mine10

        row3 = mine11 + mine12 + mine13 + mine14 + mine15

        row4 = mine16 + mine17 + mine18 + mine19 + mine20

        row5 = mine21 + mine22 + mine23 + mine24 + mine25

        info = str(random.randint(0, 75)) 
       
        em = discord.Embed(color=0x23272A)
        
        em.set_footer(text="")

        em.add_field(name="Epileps, Mines V1.2",value=row1 + "\n" + row2 + "\n" + row3 + "\n" + row4 +"\n" + row5 + "\n")
        await ctx.reply(embed=em)


bot.run("ODI5NDYwMjUzODgzNjI5Njcw.G8suNd.MIPzl7CKbeRuYulS3KTQ5yKW6wNPd8MPHYRuQU")