#bot.py - this is the brain of HoopsBot. It directly tells Discord: Here's who I am, here's what commands I can do and here's what happens when someone uses a command.
import os
import logging
import discord
from discord.ext import commands
from dotenv import load_dotenv

#local modules
from nba_data import find_game_score, find_player_stats
from summarizer import summarize_game_text

#configuration
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
BOT_PREFIX = os.getenv("BOT_PREFIX", "!")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)

logging.basicConfig(level=logging.INFO)

#Lifecycle events
@bot.event
async def on_ready():
    user = bot.user
    if user:
        print(f"[HoopsBot] Logged in as {user} (id: {user.id})")
    else:
        print("[HoopsBot] Bot logged in, but user info not available yet.")
    print("Ready to accept commands!")


#commands
@bot.command(name="score")
async def score(ctx, *, team: str):
    """
    Usage: !score Lakers
    - ctx: context of the Discord message
    - team: everything the user typed after the command (team name)
    """
    result = find_game_score(team)
    await ctx.send(result)

@bot.command(name="player")
async def player(ctx, *, name: str):
    """Usage: !player Lebron James (placeholder for now).""" 
    stats = find_player_stats(name)        #TODO: implement real stats
    await ctx.send(stats)

@bot.command(name="summary")
async def summary(ctx, *, team:str):
    """Usage: !summary Warriors - AI hype summary of the current game."""
    summary_text = summarize_game_text(team)
    await ctx.send(summary_text)

#run
if __name__ == "__main__":
    #start the bot; this basically blocks while the bot is running 
    bot.run(DISCORD_TOKEN)          