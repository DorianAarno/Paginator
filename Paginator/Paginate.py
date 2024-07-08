from disnake import ui, ButtonStyle, MessageInteraction


class PreviousButton(ui.Button):
    def __init__(self, disabled ):
        super().__init__(
            emoji="⬅️",
            style=ButtonStyle.grey,
            disabled=disabled,
            custom_id='previous'
        )

    async def callback(self, inter: MessageInteraction) -> None:
        view: CreatePaginator = self.view
        try:
            if view.author_id:
                if inter.author.id != view.author_id:
                    return await inter.send("You cannot interact with these buttons.", ephemeral=True)
            if view.current_embed:
                await inter.response.edit_message(embed=view.embeds[view.current_embed-1])
                view.current_embed = view.current_embed - 1

                if view.current_embed == 0:
                    self.disabled = True
                for btn in view.children:
                    if btn.custom_id == "next":
                        btn.disabled = False
                await inter.edit_original_message(view=view)
                
        except:
            await inter.send('Unable to change the page.', ephemeral=True)

class NextButton(ui.Button):
    def __init__(self, disabled ):
        super().__init__(
            emoji="➡️",
            style=ButtonStyle.grey,
            disabled=disabled,
            custom_id='next'
        )

    async def callback(self, inter: MessageInteraction) -> None:
        view: CreatePaginator = self.view
        try:
            if view.author_id:
                if inter.author.id != view.author_id:
                    return await inter.send("You cannot interact with these buttons.", ephemeral=True)

            await inter.response.edit_message(embed=view.embeds[view.current_embed+1])
            view.current_embed += 1

            if view.current_embed+1 == len(view.embeds):
                self.disabled = True
            for btn in view.children:
                if btn.custom_id == "previous":
                    btn.disabled = False
            await inter.edit_original_message(view=view)
            
        except:
            await inter.send('Unable to change the page.', ephemeral=True)


class CreatePaginator(ui.View):
    """
    Paginator for Embeds.
    Parameters:
    ----------
    embeds: List[Embed]
        List of embeds which are in the Paginator. Paginator starts from first embed.
    author_id: int = None (Optional)
        The ID of the author who can interact with the buttons. Anyone can interact with the Paginator Buttons if not specified.
    timeout: float = None (Optional)
        How long the Paginator should timeout in, after the last interaction.

    """
    def __init__(self, embeds, author_id: int = None, timeout: float = None):
        
        super().__init__(
            timeout=None
        )
        self.embeds = embeds
        self.author_id = author_id
        self.current_embed = 0
        
        disabled = False
        if len(embeds) == 1:
            disabled = True
        self.add_item(PreviousButton(True))
        self.add_item(NextButton(disabled))

# class CreatePaginator(ui.View):
#     """
#     Paginator for Embeds.
#     Parameters:
#     ----------
#     embeds: List[Embed]
#         List of embeds which are in the Paginator. Paginator starts from first embed.
#     author: int
#         The ID of the author who can interact with the buttons. Anyone can interact with the Paginator Buttons if not specified.
#     timeout: float
#         How long the Paginator should timeout in, after the last interaction.

#     """
#     def __init__(self, embeds: list, author: int | None = None, timeout: float | None = None):
#         if not timeout:
#             super().__init__()
#         else:
#             super().__init__(timeout=timeout)
#         self.embeds = embeds
#         self.author = author
#         self.CurrentEmbed = 0

    

#     @ui.button(emoji="⬅️", style=ButtonStyle.grey)
#     async def previous(self, button, inter):
#         if not inter.response.is_done():
#             await inter.response.defer(ephemeral=True)
#         try:
#             if inter.author.id != self.author and self.author:
#                 return await inter.followup.send("You cannot interact with these buttons.", ephemeral=True)

#             if self.CurrentEmbed:
#                 await inter.followup.edit_message(embed=self.embeds[self.CurrentEmbed-1])
#                 self.CurrentEmbed -= 1
#             else:
#                 raise ValueError("No previous embed available")

#         except Exception as e:
#             self.logger.error(f"Error in Paginator 'previous': {e}")
#             await inter.followup.send('Unable to change the page.', ephemeral=True)

#     @ui.button(emoji="➡️", style=ButtonStyle.grey)
#     async def next(self, button, inter):
#         if not inter.response.is_done():
#             await inter.response.defer(ephemeral=True)
#         try:
#             if inter.author.id != self.author and self.author != 123:
#                 return await inter.followup.send("You cannot interact with these buttons.", ephemeral=True)

#             await inter.followup.edit_message(embed=self.embeds[self.CurrentEmbed+1])
#             self.CurrentEmbed += 1

#         except Exception as e:
#             self.logger.error(f"Error in Paginator 'next': {e}")
#             await inter.followup.send('Unable to change the page.', ephemeral=True)
