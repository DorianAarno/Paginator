from disnake.ext.commands import InteractionBot
import disnake
from dotenv import load_dotenv
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Paginator import CreatePaginator

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = InteractionBot(intents=disnake.Intents.default())

@bot.event
async def on_ready():
    print("Bot is ready")
    
# Command to test the paginator
@bot.slash_command()
async def paginate(inter: disnake.ApplicationCommandInteraction):
    embeds = [disnake.Embed(title=f"Page {i+1}", description="This is an example embed.") for i in range(5)]
    paginator = CreatePaginator(embeds, author_id=inter.author.id, timeout=None)
    await inter.send(embed=embeds[0], view=paginator)

# Run the bot with your token
bot.run(BOT_TOKEN)
