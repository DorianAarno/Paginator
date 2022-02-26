<<<<<<< HEAD
# Disnake Paginator
=======
# Disnake Paginator 
>>>>>>> 6844432ca36b55dbf2689caf3a6d00cab2fdf374
A simple Embed Paginator developed for projects made with [disnake](ttps://github.com/DisnakeDev/disnake), a fork of [discord.py](https://github.com/Rapptz/discord.py).

# Installation
You can use [pip](https://pip.pypa.io/en/stable/) to install this library.
```py
<<<<<<< HEAD
pip install
```

# Usage
### Guide
```py
from Paginate import CreatePaginator
from disnake import Embed
embeds = [
=======
pip install 
```

# Usage 
### Guide 
```py
from Paginate import CreatePaginator 
from disnake import Embed 
embeds = [ 
>>>>>>> 6844432ca36b55dbf2689caf3a6d00cab2fdf374
  Embed(description="First Embed"),
  Embed(description="Second Embed"),
  Embed(description="Third Embed"),
  Embed(description="Fourth Embed")
]
timeout = 120.0 # Optional
author_id = ctx.author.id # Optional, If not specified, anyone can interact with pagination buttons.
await ctx.send(embed=embeds[0], view=CreatePaginator(ctx, embeds, author_id, timeout))
```

<<<<<<< HEAD
# Contributing
* Pull requests and issues are welcome.
* Consider giving this repository a ⭐, It is highly appreciated!

# License
This repository has been made available via [MIT](https://github.com/DorianAarno/Paginator/blob/main/LICENSE) License.
=======
# Contributing 
* Pull requests and issues are welcome. 
* Consider giving this repository a ⭐, It is highly appreciated! 

# License
This repository has been made available via [MIT](https://github.com/DorianAarno/Paginator/blob/main/LICENSE) License.
  
>>>>>>> 6844432ca36b55dbf2689caf3a6d00cab2fdf374
