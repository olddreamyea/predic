from discord.ext import commands
import discord
import random

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is online and ready to use")

#blue-FFFFFF
#redish-FFFFFF
@bot.command()
async def cup(ctx):
        predictions = ['red','red','red','blue','blue','blue','red']
        prediction = random.choice(predictions)
        if prediction == 'red':
            embed_color = 0x23272A
            color_text = 'Pick the red cup colour.'
            prediction = ""
        elif prediction == 'blue':
            embed_color = 0x23272A
            color_text = 'Pick the blue cup colour'
            prediction = ""
        
            
            
            
        em = discord.Embed(color=embed_color)
        em.add_field(name="Epileps Predictor", value=color_text + "\n" + prediction)
        em.set_footer(text="")
        await ctx.send(embed=em)
   

bot.run('ODI5NDYwMjUzODgzNjI5Njcw.G8suNd.MIPzl7CKbeRuYulS3KTQ5yKW6wNPd8MPHYRuQU')