import discord
from discord.ext import commands
from scrapper import scrape_live_score, append_to_csv, get_stats
import io
intents = discord.Intents.all()


bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print('------')

@bot.command(name="livescore")
async def livescore(ctx):
    print(f"Received !livescore command from {ctx.author.name} ({ctx.author.id})")
    respo,live_score, team1, team2= scrape_live_score()
    append_to_csv(live_score)
    await ctx.send(respo)
    await ctx.send(f"***{team1}*** **vs** ***{team2}***")
    await ctx.send(live_score)

@bot.command(name="csv")
async def csv(ctx):
    print(f"Received !csv command from {ctx.author.name} ({ctx.author.id})")
    
    with open('scores.csv', 'r') as csvfile:
        csv_content = csvfile.read()

    csv_file = discord.File(io.BytesIO(csv_content.encode()), filename='scores.csv')
    await ctx.send(file=csv_file)

@bot.command(name="hello")
async def hello(ctx):
    await ctx.send(f"Hey there {ctx.author.name}!")

@bot.command(name="stats")
async def stats(ctx):
    print(f"Received !stats command from {ctx.author.name} ({ctx.author.id})")
    statistics = get_stats()
    await ctx.send(statistics)

@bot.command()
async def commands(ctx):
    commands_list = [
        "!livescore - Get live cricket score",
        "!csv - Get the CSV file with scraped scores",
        "!stats - Get the stats for the match",
        "!hello - Greets the user with his/her username",
        "!commands - Give the list of commands",
    ]
    await ctx.send("\n".join(commands_list))

bot.run('MTE0OTQxOTMzOTM2NDE5MjI5Ng.GNIFT8.0lLxzhvj9-blyYcywwIQWlDCMcKrXwJJKK-rEU')
