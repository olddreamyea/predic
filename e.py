from discord.ext import commands
import discord
import random

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is online and ready to use")

#gold-FFFFFF
#purple-FFFFFF
#redish-FFFFFF
@bot.command()
async def case(ctx):

        predictions = ['red','purple','gold','green','black','white','blackgreen','blackyellow','blackred','blackblue','blackbluee','blackblueee','blackblueeee','blackblueeeee','blackblueeeeee','blackblueeeeeee','blackblueeeeeeee','blackblueeeeeeeee','blackblueeeeeeeeee','blackblueeeeeeeeeee','blackblueeeeeeeeeee']
        prediction = random.choice(predictions)
        if prediction == 'red':
            embed_color = 0x23272A
            color_text = 'Pick the Federation Case'
            prediction = ""
        elif prediction == 'purple':
            embed_color = 0x23272A
            color_text = 'Pick the Periastron Case'
            prediction = ""
        elif prediction == 'gold':
            embed_color = 0x23272A
            color_text = 'Pick the Valk,Case'
            prediction = ""
        elif prediction == 'green':
            embed_color = 0x23272A
            color_text = 'Pick the Bucket Case'
            prediction = ""
        elif prediction == 'black':
            embed_color = 0x23272A
            color_text = 'Pick the Antler Case'
            prediction = ""
        elif prediction == 'white':
            embed_color = 0x23272A
            color_text = 'Pick the Doge Case'
            prediction = ""
        elif prediction == 'blackgreen':
            embed_color = 0x23272A
            color_text = 'Pick the Dominus Revolution Case'
            prediction = ""
        elif prediction == 'blackyellow':
            embed_color = 0x23272A
            color_text = 'Pick the Purple Face Case'
            prediction = ""
        elif prediction == 'blackyellow':
            embed_color = 0x23272A
            color_text = 'Pick the King Case'
            prediction = ""
        elif prediction == 'blackred':
            embed_color = 0x23272A
            color_text = 'Pick the Sparkle Case'
            prediction = ""
        elif prediction == 'blackblue':
            embed_color = 0x23272A
            color_text = 'Pick the Toxic Case'
            prediction = ""
        elif prediction == 'blackbluee':
            embed_color = 0x23272A
            color_text = 'Pick the Sunglass Case'
            prediction = ""
        elif prediction == 'blackblueee':
            embed_color = 0x23272A
            color_text = 'Pick the Pink Face Case'
            prediction = ""
        elif prediction == 'blackblueeee':
            embed_color = 0x23272A
            color_text = 'Pick the Horn Case'
            prediction = ""
        elif prediction == 'blackblueeeee':
            embed_color = 0x23272A
            color_text = 'Pick the Streampunk Case'
            prediction = ""
        elif prediction == 'blackblueeeee':
            embed_color = 0x23272A
            color_text = 'Pick the Madness Case'
            prediction = ""
        elif prediction == 'blackblueeeeee':
            embed_color = 0x23272A
            color_text = 'Pick the Gold Case'
            prediction = ""
        elif prediction == 'blackblueeeeee':
            embed_color = 0x23272A
            color_text = 'Pick the Sweet Case'
            prediction = ""
        elif prediction == 'blackblueeeeee':
            embed_color = 0x23272A
            color_text = 'Pick the Super Happy Flip Case'
            prediction = ""
        elif prediction == 'blackblueeeeee':
            embed_color = 0x23272A
            color_text = 'Pick the Gold Shades Case'
            prediction = ""
        elif prediction == 'blackblueeeeeee':
            embed_color = 0x23272A
            color_text = 'Pick the D.I.Y Case'
            prediction = ""
        elif prediction == 'blackblueeeeeeee':
            embed_color = 0x23272A
            color_text = 'Pick The Balancer'
            prediction = ""
        elif prediction == 'blackblueeeeeeeee':
            embed_color = 0x23272A
            color_text = 'Pick The Budger Case'
            prediction = ""
        em = discord.Embed(color=embed_color)
        em.add_field(name="Epileps Predictor", value=color_text + "\n" + prediction)
        em.set_footer(text="")
        await ctx.send(embed=em)
    

bot.run('ODI5NDYwMjUzODgzNjI5Njcw.G8suNd.MIPzl7CKbeRuYulS3KTQ5yKW6wNPd8MPHYRuQU')