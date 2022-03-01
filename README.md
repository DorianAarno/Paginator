# Disnake Paginator
A simple Embed Paginator developed for projects made with [disnake](ttps://github.com/DisnakeDev/disnake), a fork of [discord.py](https://github.com/Rapptz/discord.py).

# Installation
You can use [pip](https://pip.pypa.io/en/stable/) to install this library.
```
pip install disnake-pagination
```

# Usage
### Guide
```py
from Paginator import CreatePaginator
from disnake import Embed

embeds = [
  Embed(description="First Embed"),
  Embed(description="Second Embed"),
  Embed(description="Third Embed"),
  Embed(description="Fourth Embed")
]
timeout = 120.0 # Optional
author_id = ctx.author.id # Optional, If not specified, anyone can interact with pagination buttons.

await ctx.send(embed=embeds[0], view=CreatePaginator(ctx, embeds, author_id, timeout))
```

# Contributing
* Pull requests and issues are welcome.
* Consider giving this repository a ⭐, It is highly appreciated!

# License
This repository has been made available via [MIT](https://github.com/DorianAarno/Paginator/blob/main/LICENSE) License.
