from disnake import *

class PaginationButtons(ui.View):
    """
    Paginator for Embeds.
    Parameters:
    ----------
    embeds: List[Embed]
        List of embeds which are in the Paginator. Paginator starts from first embed.
    author: int
        The ID of the author who can interact with the buttons. Anyone can interact with the Paginator Buttons if not specified.
    timeout: float
        How long the Paginator should timeout in, after the last interaction.

    """
    def __init__(self, embeds: list, author: int = 123, timeout: float = None):
        if not timeout:
            super().__init__()
        else:
            super().__init__(timeout=timeout)
        self.embeds = embeds
        self.author = author
        self.CurrentEmbed = 0

    @ui.button(emoji="⬅️", style=ButtonStyle.grey)
    async def next(self, button, inter):
        try:
            if inter.author.id != self.author:
                return await inter.send("You cannot interact with these buttons.", ephemeral=True)
            await inter.response.edit_message(embed=self.embeds[self.CurrentEmbed+1])
        except:
            await inter.send('Unable to change the page.', ephemeral=True)
        finally:
            self.CurrentEmbed += 1

    @ui.button(emoji="➡️", style=ButtonStyle.grey)
    async def previous(self, button, inter):
        try:
            if inter.author.id != self.author:
                return await inter.send("You cannot interact with these buttons.", ephemeral=True)
            await inter.response.edit_message(embed=self.embeds[self.CurrentEmbed-1])
        except:
            await inter.send('Unable to change the page.', ephemeral=True)
        finally:
            self.CurrentEmbed = self.CurrentEmbed - 1
