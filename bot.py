from Paginator import Paginate
from disnake.ext import commands
from disnake import Embed

bot = commands.InteractionBot()

@bot.slash_command()
async def test(ctx):
    embeds = [
        Embed(description="First Embed"),
        Embed(description="Second Embed"),
        Embed(description="Third Embed"),
        Embed(description="Fourth Embed")
    ]
    timeout = 120.0 # Optional
    author_id = ctx.author.id # Optional, If not specified, anyone can interact with pagination buttons.

    await ctx.send(embed=embeds[0], view=Paginate.CreatePaginator(embeds, ))

bot.run("ODYwNDAxMDg2Mjc1MTI1MjQ4.Gm3f7o.TU9oWQbdxHIV41xVbIpJtOQce_-Fa9A_OMTcHM")