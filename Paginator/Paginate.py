from disnake import *
import logging


class CreatePaginator(ui.View):
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

    # Configure logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    @ui.button(emoji="⬅️", style=ButtonStyle.grey)
    async def previous(self, button, inter):
        if not inter.response.is_done():
            await inter.response.defer(ephemeral=True)
        try:
            if inter.author.id != self.author and self.author != 123:
                return await inter.followup.send("You cannot interact with these buttons.", ephemeral=True)

            if self.CurrentEmbed:
                await inter.followup.edit_message(embed=self.embeds[self.CurrentEmbed-1])
                self.CurrentEmbed -= 1
            else:
                raise ValueError("No previous embed available")

        except Exception as e:
            logger.error(f"Error in Paginator 'previous': {e}")
            await inter.followup.send('Unable to change the page.', ephemeral=True)

    @ui.button(emoji="➡️", style=ButtonStyle.grey)
    async def next(self, button, inter):
        if not inter.response.is_done():
            await inter.response.defer(ephemeral=True)
        try:
            if inter.author.id != self.author and self.author != 123:
                return await inter.followup.send("You cannot interact with these buttons.", ephemeral=True)

            await inter.followup.edit_message(embed=self.embeds[self.CurrentEmbed+1])
            self.CurrentEmbed += 1

        except Exception as e:
            logger.error(f"Error in Paginator 'next': {e}")
            await inter.followup.send('Unable to change the page.', ephemeral=True)
